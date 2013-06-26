title: GUI building with Matlab
date: 2013-04-25
category: Blog
tags: GUI building, Matlab, GUIDE

The first lesson I've learned about GUI development is: _create a mockup_.

# Why avoid GUIDE (GUI development environment)

With GUIDE is possible design UIs graphically, however instead

# Create GUI programatically

    function varargout = mygui(varargin)
        % Brief description
        sizeScreen = get(0,'ScreenSize')
        hmf = figure('Position', sizeScreen,...
               'Name', 'Mammogram GUI',...
               'NumberTitle', 'off',...
               'MenuBar', 'none');

        eth = uicontrol(hmf, 'Style','edit',...
                        'String','Enter your name here.',...
                        'Position',[130 150 130 120]);
    end

In the code above we have create a basic window.
