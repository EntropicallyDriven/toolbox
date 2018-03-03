import tkinter as tk
import tkinter.filedialog as tkf
import tkinter.messagebox as tkm
import numpy as np
import re
import os
import datetime
import xrdmlRead as xr

def dataImport(filelist, columndicts):
	output = []
	for jj,f in enumerate(filelist):
		varmap = {key.lower():columndicts[jj][key] for key in columndicts[jj]}
		varindices = []
		varnames = []
		out = {}
		file = open(f, 'r')
		
		if re.search('\.dat', f) is not None:
			fheads = file.readline().strip('\n').split('\t')
			for ii,fh in enumerate(fheads):
				try:
					varname = varmap[fh.lower()]
					
					if varname not in varnames:
						varnames.append(varname)
						out[varname] = []
					varindices.append(ii)
				except KeyError:
					pass

			data = file.readlines()
			for line in data:
				vals = line.strip('\n').split('\t')
				selvals = [vals[index] for index in varindices]
				if '-' in selvals:
					pass
				else:
					for ii, val in enumerate(selvals):
						try:
							newval = float(val)
							if np.abs(newval) == float('Inf'):
								newval = val
						except ValueError:
							try:
								newval = datetime.datetime.strptime(val, '%Y-%m-%d %H:%M:%S.%f')
							except ValueError:
								pass
						out[varnames[ii]].append(newval)
			
			for key in out.keys():
				if isinstance(out[key][0], float): 
					out[key] = np.array(out[key])
			
			output.append(out)
			file.close()
		else:
			print('only .dat files work!')
			raise NotImplementedError
	
	print('GENERATED!')
	print(filelist)
	print(varnames)
	return output

def dataImportFull(filelist, columndicts):
	output = []
	for jj,f in enumerate(filelist):
		varmap = {key.lower():columndicts[jj][key] for key in columndicts[jj]}
		varindices = []
		varnames = []
		out = {}
		file = open(f, 'r')
		
		if re.search('\.dat', f) is not None:
			fheads = file.readline().strip('\n').split('\t')
			for ii,fh in enumerate(fheads):
				try:
					varname = varmap[fh.lower()]
					
					if varname not in varnames:
						varnames.append(varname)
						out[varname] = []
					varindices.append(ii)
				except KeyError:
					pass

			data = file.readlines()
			for line in data:
				vals = line.strip('\n').split('\t')
				selvals = [vals[index] for index in varindices]
				for ii, val in enumerate(selvals):
					if val == '-':
						out[varnames[ii]].append(None)
					else:
						try:
							newval = float(val)
							if np.abs(newval) == float('Inf'):
								newval = val
						except ValueError:
							try:
								newval = datetime.datetime.strptime(val, '%Y-%m-%d %H:%M:%S.%f')
							except ValueError:
								newval=val
						out[varnames[ii]].append(newval)
			
			output.append(out)
			file.close()
		else:
			print('only .dat files work!')
			raise NotImplementedError
	
	print('GENERATED!')
	print(filelist)
	print(varnames)
	return output
	
class dataReader:
    def __init__(self):
        self.output = None
        self.fnames = []
        self.window = tk.Tk()
        tk.Label(self.window, text='Folder:').grid(row=0, column=0, sticky='NSEW')
        self.activeFolder = tk.Entry(self.window, width=75)
        self.activeFolder.grid(row=0, column=1, columnspan=2, sticky='NSEW')
        tk.Button(self.window, text='Select', command=self.chooseFolder).grid(row=0, column=3, sticky='NSEW')
        
        self.window.grid_columnconfigure(0, weight=0)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_columnconfigure(2, weight=1)
        self.window.grid_columnconfigure(3, weight=0)
        self.window.grid_columnconfigure(4, weight=0)
        self.window.grid_columnconfigure(5, weight=0)
        self.window.grid_columnconfigure(6, weight=1)
        
        self.filelist = tk.Listbox(self.window, height=10, selectmode=tk.MULTIPLE, exportselection=0)
        self.filelist.grid(row=1, column=0, columnspan=4, rowspan=10, sticky='NSEW')
        self.filelist.bind("<<ListboxSelect>>", self.updateHeaders)
        
        tk.Button(self.window, text='select all', command=self.selectall).grid(row=11, column=0, columnspan=2, sticky='NSEW')
        tk.Button(self.window, text='select none', command=self.selectnone).grid(row=11, column=2, columnspan=2, sticky='NSEW')
        
        self.mode = tk.IntVar()
        self.mode.set(1)

        tk.Radiobutton(self.window, text="create indexed list", variable=self.mode, value=1).grid(row=12, column=1, sticky='NSEW')
        tk.Radiobutton(self.window, text="combine all files", variable=self.mode, value=2).grid(row=12, column=2, sticky='NSEW')
        
        genbutton = tk.Button(self.window, text = 'GENERATE', command=self.generate).grid(row=13, column=0, columnspan=4, sticky='NSEW')
        
        self.headers = []
        self.headlabels = []
        self.colboxes = []
        self.saveboxes = []
        self.savetraces = []
        
        self.window.grab_set()
        
        tk.mainloop()

    def generate(self):
        currentvarnames = [xx.get() for xx in self.colboxes]
        for ii in range(len(currentvarnames))[::-1]:
            if not self.savevars[ii].get():
                del currentvarnames[ii]
        if len(currentvarnames) != len(set(currentvarnames)):
            tkm.showerror(title='Nope', message="Your variable names aren't unique.")
        else:
            try:
                allfiles = os.listdir(self.activeFolder.get())
                selection = self.filelist.curselection()
                if len(selection)==0:
                    return
                files = [allfiles[sel] for sel in selection]
                varmap = {}
                for ii, head in enumerate(self.headers):
                    if self.savevars[ii].get():
                        varmap[head.lower()] = self.colboxes[ii].get()

            except FileNotFoundError:
                return

            if self.mode.get() == 1:   #Selected to create indexed list of dicts
                self.output = []
                for f in files:
                    varindices = []
                    varnames = []
                    self.out = {}
                    file = open(self.activeFolder.get()+'/'+f)
                    
                    if re.search('\.dat', f) is not None:
                        fheads = file.readline().strip('\n').split('\t')
                        for ii,fh in enumerate(fheads):
                            try:
                                varname = varmap[fh.lower()]
                                
                                if varname not in varnames:
                                    varnames.append(varname)
                                    self.out[varname] = []
                                varindices.append(ii)
                            except KeyError:
                                pass
    
                        data = file.readlines()
                        for line in data:
                            vals = line.strip('\n').split('\t')
                            selvals = [vals[index] for index in varindices]
                            if '-' in selvals:
                                pass
                            else:
                                for ii, val in enumerate(selvals):
                                    try:
                                        val = float(val)
                                    except ValueError:
                                        try:
                                            val = datetime.datetime.strptime(val, '%Y-%m-%d %H:%M:%S.%f')
                                        except ValueError:
                                            pass
                                    self.out[varnames[ii]].append(val)
                        
                        for key in self.out.keys():
                            if isinstance(self.out[key][0], float): 
                                self.out[key] = np.array(self.out[key])
                        
                        self.output.append(self.out)
                        self.fnames.append(f)
                        file.close()                        
                        
                    elif re.search('\.xrdml', f) is not None:
                        vacancies = 0
                        fheads = xr.getHeaders(file)
                        fdata = xr.getData(file)
                        for ii,fh in enumerate(fheads):
                            try:
                                varname = varmap[fh.lower()]
                                if varname not in varnames:
                                    varnames.append(varname)
                                    self.out[varname] = []
                                self.out[varnames[ii-vacancies]] = fdata[ii]
                            except KeyError:
                                vacancies +=1 
                                pass
                            
                        for key in self.out.keys():
                                if isinstance(self.out[key][0], float):
                                    self.out[key] = np.array(self.out[key])

                        self.output.append(self.out)
                        self.fnames.append(f)
                        file.close()                        

            else:  # merge into single dict
                for f in files:
                    if re.search('\.xrdml', f) is not None:
                        tkm.showerror(title='Nope', message="Agglomeration of data not supported for XRDML files...yet.")
                        return
                self.output = {}
                for f in files:
                    varindices = []
                    varnames = []
                    file = open(self.activeFolder.get()+'/'+f)
                    fheads = file.readline().strip('\n').split('\t')
                    for ii,fh in enumerate(fheads):
                        try:
                            varname = varmap[fh.lower()]
                            
                            if varname not in varnames:
                                varnames.append(varname)
                                self.output[varname] = []
                            varindices.append(ii)
                        except KeyError:
                            pass

                    data = file.readlines()
                    for line in data:
                        vals = line.strip('\n').split('\t')
                        selvals = [vals[index] for index in varindices]
                        if '-' in selvals:
                            pass
                        else:
                            for ii, val in enumerate(selvals):
                                try:
                                    val = float(val)
                                except ValueError:
                                    try:
                                        val = datetime.datetime.strptime(val, '%Y-%m-%d %H:%M:%S.%f')
                                    except ValueError:
                                        pass
                                self.output[varnames[ii]].append(val)
                    
                    for key in self.output.keys():
                        if isinstance(self.output[key][0], float):
                            self.output[key] = np.array(self.output[key])
                    
                    self.fnames.append(f)
                    file.close()

        
        print('GENERATED!')
        print(files)
        print(varnames)
    
    def getOutput(self):
        return self.output, self.fnames
        
    def chooseFolder(self):
        try:
            foldername = tkf.askdirectory()
            self.activeFolder.delete(0, tk.END)
            self.activeFolder.insert(0, foldername)
            files = os.listdir(foldername)
            self.filelist.delete(0,tk.END)
            for file in files:
                self.filelist.insert(tk.END, file)
        except FileNotFoundError:
            self.activeFolder.delete(0, tk.END)
            self.filelist.delete(0,tk.END)
    
    def selectall(self):
        self.filelist.selection_set(0, tk.END)
        self.updateHeaders()
    
    def selectnone(self):
        self.filelist.select_clear(0, tk.END)
        self.updateHeaders()
    
    def updateHeaders(self, *args):
        if self.activeFolder.get() == '':
            pass
        else:
            oldheads = [xx.lower() for xx in self.headers]
            oldvarnames = [xx.get() for xx in self.colboxes]
            for ii in range(len(self.headers)):
                try:
                    self.headlabels[ii].destroy()
                    self.saveboxes[ii].destroy()
                    self.colboxes[ii].destroy()
                except TypeError:
                    pass
            self.headlabels = []
            self.headers = []
            self.colboxes = []
            self.saveboxes=[]
            self.savevars = []
            
            # GET LIST OF FILES
            allfiles = os.listdir(self.activeFolder.get())
            selection = self.filelist.curselection()
            files = [allfiles[sel] for sel in selection]
            
            # LOOP THROUGH FILES
            for f in files:
                file = open(self.activeFolder.get()+'/'+f)
                if re.search('\.dat', f) is not None:
                    fheads = file.readline().strip('\n').split('\t')
                elif re.search('\.xrdml', f) is not None:
                    fheads = xr.getHeaders(file)
                for fh in fheads:
                    if fh not in self.headers:
                        if fh.lower() not in [xx.lower() for xx in self.headers]:
                            self.headers.append(fh)                    
                file.close()
                
                
            self.headers = sorted(self.headers)
            for ii, hh in enumerate(self.headers):
                self.headlabels.append(tk.Label(self.window, text=hh, width=50, justify="right"))
                self.headlabels[-1].grid(row=1+ii, column=4, sticky='NSE')
                self.savevars.append(tk.BooleanVar())
                self.savevars[-1].set(False)
                self.savevars[-1].trace("w", lambda v, n, m, ii=ii: self.updatesave(v, n, m, ii))
                self.saveboxes.append(tk.Checkbutton(self.window, variable=self.savevars[-1]))
                self.saveboxes[-1].grid(row=1+ii, column=5, sticky='NSW')
                self.colboxes.append(tk.Entry(self.window, width=50))
                self.colboxes[-1].grid(row=1+ii, column=6, sticky='NSW')

                if hh.lower() in oldheads:
                    num = sorted(oldheads).index(hh.lower())
                    self.colboxes[-1].delete(0, tk.END)
                    self.colboxes[-1].insert(0, sorted(oldvarnames)[num])
                else:
                    self.colboxes[-1].delete(0, tk.END)
                    self.colboxes[-1].insert(0, hh.split('--')[-1].split(r' ')[0].lower())
                self.colboxes[-1].config(state='disabled')
                
    def updatesave(self,v,n,m,ii):
        if self.savevars[ii].get():
            self.colboxes[ii].config(state='normal')
        else:
            self.colboxes[ii].config(state='disabled')

def activate(dat):
    for key in dat.keys():
        exec("global {:s}".format(key), globals(), globals())
        exec("{:s} = dat['{:s}']".format(key,key), locals(), globals())
        
