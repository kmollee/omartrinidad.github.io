title: GUI building with Matlab
date: 2013-04-25
category: Blog
tags: GUI building, Matlab, GUIDE

The first lesson I've learned about GUI development is: _create a mockup_. The
first step in this little tutorial it will be draw our objective.

-IMAGEN-

Here, we have a simple GUI, with a left panel and an axe.

# Why avoid GUIDE (GUI development environment)

With GUIDE is possible design UIs graphically, however instead of making it
easier complicates it. In order to have a better control and understanding of
the things I prefer create the GUI programmatically.

# Create GUI programmatically

    function varargout = mygui(varargin)
        % Brief description
        sizeScreen = get(0,'ScreenSize')
        hmf = figure('Position', sizeScreen,...
               'Name', 'Mammogram GUI',...
               'NumberTitle', 'off',...
               'MenuBar', 'none');
    end

In the code above we have create a _very_ basic window.

# Adding controls with <code>uicontrol</code>

# Adding menues with <code>uimenus</code>

# Callbacks and functions

# Share data

The most easy way to share data is using _nested functions_. With this approach
we can 
