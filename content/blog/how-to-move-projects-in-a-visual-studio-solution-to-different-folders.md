+++
title = "How to move projects in a Visual Studio Solution to different folders?"
description = ""
date = 2019-03-29T11:11:48
updated = 2019-03-29T13:01:11
draft = false
slug = "how-to-move-projects-in-a-visual-studio-solution-to-different-folders"
aliases = ['2019/03/29/how-to-move-projects-in-a-visual-studio-solution-to-different-folders/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = []
+++


I was given a simple task of moving the project folders inside a Visual Studio
Solution to a different folder because even though we were using Solution
Folders feature of Visual Studio, on disk, there were a lot of folders and
adding them inside the CI pipelines' path filters was a pain to add and
maintain.

This solution was already a part of Git Source Control, had internal
dependencies and I wanted to do this and commit my changes with minimal fuss.

Credits -- https://stackoverflow.com/a/6310570

Follow the below steps to move the projects -

 1. Open CMD/PowerShell (I am on Windows...)
    
    
 2. Create the nested folder structure to where you would be moving the folders.
    You can either use mkdir or the Explorer to create new folders.
    
    
 3. Now, at the root folder of the solution, type in git mv <source_folder>
    <destination_location>
    Before actually moving the folder, you can also add the --dry-run switch at
    the end to see what changes would be made and errors which might come (if
    any).
    In case you get an error because permission was denied, ensure that the
    project is closed in Visual Studio. This happens especially with the
    Database projects.
    
    
 4. Now, if you open the destination path, you will notice that the project
    folder has moved.
    
    
 5. After doing this if you try opening the solution, Visual Studio will
    complain that it was unable to load the projects which is fine.
    
    
 6. To fix this, you can either
    a. Open the Solution File (.SLN) in Notepad and fix the paths in there
    b. In Solution Explorer, Remove the project and then right click on the
    Solution -> Add -> Existing Project -> Select the Project File at the new
    path.
    
    
 7. After adding the projects, you would have to remove the Project Dependencies 
    and then add them again.
    
    
 8. Once you have re-added the dependencies correctly, your solution should
    build.