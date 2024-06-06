# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 15:58:39 2023

@author: Bahadır Yüzlü
"""
import sqlite3
import PySimpleGUI as sg
import numpy as np

con = sqlite3.connect('database.db')
cur = con.cursor()
default_window_size = (1000, 600)
admin_name = ""
running = True

# Phase 1 Window
def initial_window():
    global window
    layout = [[sg.Text('', size=(20, 4))],
              [sg.Button('Admin', size=20)],
              [sg.Button('Candidate', size=20)]]
    return sg.Window('Initial Window', layout, size=default_window_size, element_justification='c')

# Phase 2 Windows
def admin_login_window():
    global window
    layout = [[sg.Text('', size=(25, 4))],
              [sg.Text('Enter Admin Name', size=(20, 4))],
              [sg.Input(key="adminname",size = 30)],
              [sg.Button('Log in',key="login", size=20)],
              [sg.Button("Go back",key="goback1")]]
    
    return sg.Window('Admin Log In', layout, size=default_window_size, element_justification='c')

# Phase 3 Windows
def admin_window():
    global window
    layout = [[sg.Text('', size=(20, 4))],
              [sg.Button('Add Candidate', size=20)],
              [sg.Button('Evaluate Candidate', size=20)],
              [sg.Button('Create Criterion List', size=20)],
              [sg.Button('Results', size=20)],
              [sg.Button('Log out', key="logout", size=20)]]
    return sg.Window('Admin', layout, size=default_window_size, element_justification='c')


def candidate_window():
    global window
    layout = [[sg.Text('', size=(25, 4))],
              [sg.Text('', size=(5, 1)), sg.Text('Name', size=(22, 1)),
               sg.Input(key='candidate_name', size=30)],
              [sg.Text('', size=(5, 1)), sg.Text('', size=(22, 1)), sg.Button(
                  'Submit', key="submit1", size=9)],
              [sg.Text('', size=(5, 1)), sg.Text('', size=(22, 1)), sg.Button(
                  'Log out', key="logout", size=9)]]
    return sg.Window('Candidate', layout, size=default_window_size, element_justification='c')



# Phase 4 Windows
def admin_candidate_add_window():
    global window
    layout = [[sg.Text('', size=(25, 4))],
              [sg.Text('', size=(5, 1)), sg.Text('Name', size=(22, 1)),
               sg.Input(key='candidate_name', size=30)],
              [sg.Text('', size=(5, 1)), sg.Text('', size=(22, 1)), sg.Button(
                  'Submit', key="submit2", size=9)],
              [sg.Text('', size=(5, 1)), sg.Text('', size=(22, 1)), sg.Button(
                  'Go back', key="goback2", size=9)]]
    return sg.Window('Candidate', layout, size=default_window_size, element_justification='c')

def admin_evaluation_matching_window():
    global window
    # list criterion list
    criterion_lists = []
    cur.execute('SELECT crName FROM CriterionList')
    all_criterions = cur.fetchall()
    for criterionlist in all_criterions:
        criterion_lists.append(criterionlist)
    # list candidates
    candidate_list = []
    cur.execute('SELECT cName FROM Candidate')
    all_candidates = cur.fetchall()
    for candidate in all_candidates:
        candidate_list.append(candidate)

    layout = [[sg.Text('', size=(25, 2))],
              [sg.Text('Criterions', size=(10, 10)),
               sg.Combo(criterion_lists, key="chosen_criterion", size=(60, 10))],
              [sg.Text('', size=(25, 2))],
              [sg.Text('Candidates', size=(10, 10)),
               sg.Combo(candidate_list, key="chosen_candidate", size=(60, 10))],
              [sg.Text('', size=(10, 1)), sg.Button(
                  'Submit', key="submit3", size=30)],
              [sg.Text('', size=(10, 1)), sg.Button('Go back', key='goback3')]]
    return sg.Window('Evaluate Candidate', layout, size=default_window_size, element_justification='c')

def admin_create_criterion_list_window():
    global window
    layout = [[sg.Text('', size=(25, 4))],
              [sg.Text('', size=(5, 1)), sg.Text('Enter criterion name:', size=(22, 1)),
               sg.Input(key='criterionname', size=30)],
              [sg.Text('', size=(5, 1)), sg.Text('Enter trait number(max6):', size=(22, 1)),
               sg.Input(key='criterionnum', size=30)],
              [sg.Text('', size=(5, 1)), sg.Text('', size=(22, 1)), sg.Button(
                  'Submit', key="submit4", size=9)],
              [sg.Text('', size=(5, 1)), sg.Text('', size=(22, 1)), sg.Button(
                  'Go back', key="goback4", size=9)]]
    return sg.Window('Create New Criterion List', layout, size=default_window_size, element_justification='c')

def admin_show_results_window():
    global window
    # list criterion list
    criterion_lists = []
    cur.execute('SELECT crName FROM CriterionList')
    all_criterions = cur.fetchall()
    for criterionlist in all_criterions:
        criterion_lists.append(criterionlist)

    layout = [[sg.Text('', size=(25, 2))],
              [sg.Text('Criterions', size=(10, 10)),
                sg.Combo(criterion_lists, key="chosen_criterion", size=(60, 10))],
              [sg.Text('', size=(25, 2))],
              [sg.Text('', size=(10, 1)), sg.Button(
                  'Submit', key="submit5", size=30)],
              [sg.Text('', size=(10, 1)), sg.Button('Go back', key='goback5')]]
    return sg.Window('Choose a Criterion', layout, size=default_window_size, element_justification='c')


# Phase 5 Windows
def admin_evaluation_window():
    global window
    global trait_num
    cur.execute('''SELECT * FROM CriterionList where crName = ?''',(values["chosen_criterion"]))
    criterion = cur.fetchall()
    trait_names=[]
    for i in criterion:
        trait_names.append(i)
    trait_num = -1
    for i in trait_names[0][1:7]:
        trait_num+=1
        if i is None or i == "" or i == " ":
            break
    layout = [[sg.Text('', size=(25, 4))],
          [sg.Text('Evaluate traits out of 0 to 10', size=(40, 1))]]
    
    for i in range(trait_num):
        layout.append([sg.Text(f"{trait_names[0][1:7][i]}", size=(22, 1)),sg.Input(key= f"trait{i}", size=30)])
        
    layout.append([sg.Text('', size=(5, 1)), sg.Text('', size=(22, 1)), sg.Button(
        'Submit', key="submit6", size=9)])
    layout.append([sg.Text('', size=(5, 1)), sg.Text('', size=(22, 1)), sg.Button(
        'Go back', key="goback6", size=9)])
    
    return sg.Window('Create New Criterion List', layout, size=default_window_size, element_justification='c')

def admin_create_criterion_list_window2():
    global window 
    
    layout = [[sg.Text('', size=(25, 4))],
          [sg.Text('Enter the criterion on left blocks, enter the weight of it on right blocks', size=(50, 1))]]
    
    for i in range(int(chosen_trait_num)):
        layout.append([sg.Text(f"Criterion{i+1}", size=(15, 1)),sg.Input(key= f"criterionname{i+1}", size=30),sg.Input(key=f"criterionweight{i+1}",size=(5))])
        
    layout.append([sg.Text('', size=(5, 1)), sg.Text('', size=(22, 1)), sg.Button(
        'Submit', key="submit7", size=9)])
    layout.append([sg.Text('', size=(5, 1)), sg.Text('', size=(22, 1)), sg.Button(
        'Go back', key="goback7", size=9)])
    
    return sg.Window('Create New Criterion List', layout, size=default_window_size, element_justification='c')
    
def admin_show_results_window2():
    global window
    global admin_name
    chosen_criterion = str(values["chosen_criterion"][0])
    candidates = []
    cur.execute('''Select * from Evaluate where aID in (select aID from Admin where aName = ? ) and crName = ? order by OverallPoint desc''',(admin_name,chosen_criterion))
    candidate = cur.fetchall()
    for i in candidate:
        candidates.append(i)
    layout = [[sg.Text('', size=(20, 4))],
              [sg.Text(f'Candidate Points For {chosen_criterion}:', size=(40, 1))],
              [sg.Text('', size=(5,1)), sg.Text('Candidates:', size=(10,10))],
              [sg.Listbox(candidates ,size=(70, 10))],
              [sg.Button('Go Back', key='goback8', size=20)]]
    return sg.Window('Results', layout, size=default_window_size, element_justification='c')

# Buttons
def login_button(values):
    global window
    global admin_name
    while True:
        admin_name = values["adminname"]
        admins = []
        cur.execute("Select aName from Admin")
        admin = cur.fetchall()
        for i in admin:
            admins.append(i[0])
        if admin_name == "":
            sg.popup("Admin name should not be empty")
            break
        elif admin_name in admins:
            window.close()
            window = admin_window()
            sg.popup(f"Welcome to app {admin_name}")
            con.commit()
            break
        else:
            sg.popup("This name does not belong to an admin")
            break

def submit1_button(values):
    global window
    global name
    while True:
        #input candidate name 
        name = values["candidate_name"]
        names=[]
        cur.execute("Select cName from Candidate")
        all_name = cur.fetchall()
        for i in all_name:
            names.append(i[0])
        if values["candidate_name"] == "":
            sg.popup("This area can not be empty")
            break
        elif name[0].isnumeric() == 1:
            sg.popup("This area should contain some strings to be more specific")
            break
        elif " " in values["candidate_name"]:
            sg.popup("This area should not contain empty characters")
            break
        elif name in names:
            sg.popup("Name is already in candidate list")
            break
        else:
            #find maximum id and cost new id
            ID_list = []
            cur.execute("Select cID from candidate")
            all_cID = cur.fetchall()
            for i in all_cID:
                ID_list.append(i[0])
            max_cID = max(ID_list)+1
            cur.execute('''INSERT INTO Candidate VALUES (?,?)''', (max_cID, name))
            window.close()
            window = candidate_window()
            con.commit()
            sg.popup("Successfully applied!")
            break 
def submit2_button(values):
    global window
    while True:
        #input candidate name 
        name = values["candidate_name"]
        names=[]
        cur.execute("Select cName from Candidate")
        all_name = cur.fetchall()
        for i in all_name:
            names.append(i[0])
        if values["candidate_name"] == "":
            sg.popup("This area can not be empty")
            break
        elif name[0].isnumeric() == 1:
            sg.popup("This area should contain some strings to be more specific")
            break
        elif " " in values["candidate_name"]:
            sg.popup("This area should not contain empty characters")
            break
        elif name in names:
            sg.popup("Name is already in candidate list")
            break
        else:
            #find maximum id and cost new id
            ID_list = []
            cur.execute("Select cID from candidate")
            all_cID = cur.fetchall()
            for i in all_cID:
                ID_list.append(i[0])
            max_cID = max(ID_list)+1
            cur.execute('''INSERT INTO Candidate VALUES (?,?)''', (max_cID, name))
            window.close()
            window = admin_candidate_add_window()
            con.commit()
            sg.popup("Successfully applied!")
            break 
def submit3_button(values):
    global window
    global cID
    global aID
    global chosen_criterion
    while True:
        #choose criterion name
        chosen_criterion = values["chosen_criterion"]
        chosen_candidate = values["chosen_candidate"]
        if chosen_criterion == "":
            sg.popup("Criterion should not be empty")
            break
        elif chosen_candidate == "":
            sg.popup("Candidate should not be empty")
            break
        else:
            #pull relevant inputs and create an evaluate row in db
            cur.execute('''SELECT cID FROM Candidate WHERE cName =?''',(chosen_candidate))
            cID = cur.fetchone()[0]
            cur.execute('''SELECT aID FROM Admin WHERE aName = ?''',(admin_name,))
            aID = cur.fetchone()[0]
            try:
                cur.execute('''INSERT INTO Evaluate VALUES (?,?,?,?,?,?,?,?,?,?)''',(cID,aID,str(chosen_criterion[0]),"","","","","","",""))
                con.commit()
                window.close()
                window = admin_evaluation_window()
                sg.popup("Successfully applied!")
                break
            except:
                sg.popup("Evaluation already exists. You are going to update it!")
                window.close()
                window = admin_evaluation_window()
                break
def submit4_button(values):
    global window
    global chosen_trait_num
    global chosen_criterion_name
    while True:
        chosen_criterion_name = values["criterionname"]
        chosen_trait_num = values["criterionnum"]
        #inspect the restrictions
        if chosen_criterion_name == "" or chosen_criterion_name == " " or chosen_criterion_name == "   ":
            sg.popup("Trait name should not be empty")
            break
        elif chosen_trait_num.isnumeric() == 0:
            sg.popup("Trait numbers should be numeric")
            break
        elif int(chosen_trait_num) > 6 or int(chosen_trait_num) < 1:
            sg.popup("Trait number should be more than 1 and less than 6")
            break
        else:
            #input the number of desired trait(s) in desired criterion list (MAX 6)
            window.close()
            sg.popup("Processing")
            window = admin_create_criterion_list_window2()
            break
def submit5_button(values):
    global window
    while True:
        # input the desired criterion and lists candidates
        chosen_criterion = values["chosen_criterion"]
        if chosen_criterion == "":
            sg.popup("Criterion should not be empty")
            break
        else:
            window.close()
            sg.popup("Processing")
            window = admin_show_results_window2()
            break
def submit6_button(values):
    global window
    while True:
        # create a list by the evaluations taken
        Evaluations = np.array([])
        # input the evaluations and update evaluate table
        try:
            for i in range(trait_num):
                Evaluation = values[f"trait{i}"] 
                Evaluations = np.append(Evaluations,int(Evaluation))
            if any(Evaluations > 10) or any(Evaluations < 0):
                sg.popup("All of the evaluations should be on interval [0,10]")
                break
            else:
                for i in range(trait_num):
                    Evaluation = values[f"trait{i}"]
                    cur.execute(f"Update Evaluate Set Evaluation{i+1}=? where aID=? and cID=? and crName =?",(Evaluation,aID,cID,str(chosen_criterion[0])))
                # calculate overall point and update related table
                overall_point = 0
                cur.execute('''Select Weight1,Weight2,Weight3,Weight4,Weight5,Weight6 from CriterionList where crName = ?''',(str(chosen_criterion[0]),))
                weights = cur.fetchall()
                for i in range(trait_num):
                    partial_point = float(values[f"trait{i}"])*float(weights[0][i])/10
                    overall_point += partial_point
                overall_point = format(overall_point,".3f")
                cur.execute("Update Evaluate Set OverallPoint=? where aID=? and cID=? and crName =?",(overall_point,aID,cID,str(chosen_criterion[0])))
                con.commit()
                window.close()
                window = admin_window()
                sg.popup("Evaluation successful")
                break
        except:
            sg.popup("All of the evaluations should be 'filled' with 'figures' ")
            break
def submit7_button(values):
    global window
    while True:
        violate_num = 0 
        for i in range(int(chosen_trait_num)):
            if values[f"criterionname{i+1}"] == "":
                violate_num +=1
                sg.popup("All of the variables should be filled in this page")
                break
            elif values[f"criterionweight{i+1}"] == "":
                violate_num +=1
                sg.popup("All of the variables should be filled in this page")
                break
            elif values[f"criterionweight{i+1}"].isnumeric() == 0:
                violate_num +=1
                sg.popup("All of the weights should be number type")
                break
        if violate_num == 0:
            traits = {"trait1":"","trait2":"","trait3":"","trait4":"","trait5":"","trait6":""}
            weights = {"weight1":"","weight2":"","weight3":"","weight4":"","weight5":"","weight6":""}
            total_weight = 0
            for i in range(int(chosen_trait_num)):
                traits[f"trait{i+1}"] = values[f"criterionname{i+1}"]
            for i in range(int(chosen_trait_num)):
                total_weight+= float(values[f"criterionweight{i+1}"])
            for i in range(int(chosen_trait_num)):
                weights[f"weight{i+1}"] = float(values[f"criterionweight{i+1}"])/total_weight
            cur.execute('''INSERT INTO CriterionList VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)''',(chosen_criterion_name,traits["trait1"],traits["trait2"],traits["trait3"],traits["trait4"],traits["trait5"],traits["trait6"],weights["weight1"],weights["weight2"],weights["weight3"],weights["weight4"],weights["weight5"],weights["weight6"]))             
            con.commit()
            window.close()
            window = admin_window()
            sg.popup("Criterion Created")
            break
        break
        
window = initial_window()
while running:
    event,values = window.read()
    # Phase 1
    if event == "Admin":
        window.close()
        window = admin_login_window()
    elif event == "Candidate":
        window.close()
        window = candidate_window()
    # Phase 2
    elif event == "login":
        login_button(values)
    elif event == "goback1":
        window.close()
        window = initial_window()
    # Phase 3
    elif event == "Add Candidate":
        window.close()
        window = admin_candidate_add_window()
    elif event == "Evaluate Candidate":
        window.close()
        window = admin_evaluation_matching_window()
    elif event == "Create Criterion List":
        window.close()
        window = admin_create_criterion_list_window()
    elif event == "Results":
        window.close()
        window = admin_show_results_window()
    elif event == "submit1":
        submit1_button(values) 
    elif event == "logout":
        window.close()
        window = initial_window()
    # Phase 4
    elif event == "submit2":
        submit2_button(values)
    elif event == "goback2":
        window.close()
        window = admin_window()
    elif event == "submit3":
        submit3_button(values)
    elif event == "goback3":
        window.close()
        window = admin_window()
    elif event == "submit4":
        submit4_button(values)
    elif event == "goback4":
        window.close()
        window = admin_window()
    elif event == "submit5":
        submit5_button(values)
    elif event == "goback5":
        window.close()
        window = admin_window()
    # Phase 5
    elif event == "submit6":
        submit6_button(values)
    elif event == "goback6":
        window.close()
        window = admin_evaluation_matching_window()
    elif event == "submit7":
        submit7_button(values)
    elif event == "goback7":
        window.close()
        window = admin_create_criterion_list_window()
    elif event == "goback8":
        window.close()
        window = admin_show_results_window()
        
    # Buttons
    # Closing statements
    elif event == sg.WIN_CLOSED:
        running = False
con.commit()
window.close()
