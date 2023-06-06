/* -*- mode: c++; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- */

/* 
 * MainWindow.hpp 
 *
 * This file is part of the Chemical Data Processing Toolkit
 *
 * Copyright (C) 2003 Thomas Seidel <thomas.seidel@univie.ac.at>
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2 of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this program; see the file COPYING. If not, write to
 * the Free Software Foundation, Inc., 59 Temple Place - Suite 330,
 * Boston, MA 02111-1307, USA.
 */


#ifndef CHOX_MAINWINDOW_HPP
#define CHOX_MAINWINDOW_HPP

#include <vector>

#include <QMainWindow>

#include "ui_MainWindow.h"
#include "CDPLFwd.hpp"


class QLabel;
class QFileDialog;
class QMenu;
class QActionGroup;
class QAction;

namespace ChOX { class DataSetView; }
namespace ChOX { class DataSet; }
namespace ChOX { class DataSetViewControl; }
namespace ChOX { class Settings; }
namespace ChOX { class SettingsEditDialog; }
namespace ChOX { class RangeSelectionDialog; }


namespace ChOX
{

	class MainWindow : public QMainWindow
	{
		Q_OBJECT

	public:
		MainWindow(QWidget* parent = 0, Qt::WindowFlags f = 0);
		~MainWindow();

		bool openFiles(const QStringList & file_names);

	public slots:
		void init();

		void fileNew();
		void fileOpen();
		void fileSaveAs();
		void fileSaveSelectionAs();
		void fileAppend();
		void filePrint();
		void fileQuit();
		void helpAbout();

	private slots:
		void destroy();
		void selectRecordRange();
		void editSettings();
		void handleNumColumnsChange(int num_cols);
		void handleNumRowsChange(int num_rows);
		void handleDataSetSizeChange(int new_size);
		void handleSelectionStatusChange(bool selected);
		void handleViewSettingsChange(int);
		void showErrorMessage(const QString& msg);
		void showStatusMessage(const QString& msg);
		void updateCaption();
		void recentFileSelected(QAction* action);
		void setupRecentFilesMenu();
		void setupWindowMenu();
		void tileWindows();
		void cascadeWindows();
		void setWindowActive();
		void handleControlParamChange(const CDPL::Base::LookupKey& key, const CDPL::Base::Any& val);
		void viewAlignmentChanged();
		void viewSizeAdjustmentChanged();
		void reactionArrowStyleChanged();
		void reactionAgentAlignmentChanged();
		void reactionAgentLayoutStyleChanged();
		void reactionAgentLayoutDirChanged();
		void reactionCompLayoutStyleChanged();
		void reactionCompLayoutDirChanged();
		void viewReactionSettingsChanged(bool checked);
		void viewBondSettingsChanged(bool checked);
		void viewAtomSettingsChanged(bool checked);
		void saveSettings();

	private:
		void setupContextMenu();

		void setupNewWindow(MainWindow* window);

		void setupFileOpenDialog(bool all_types);
		void setupFileSaveDialog();

		void closeEvent(QCloseEvent* e);

		void handleSizeAdjustmentChange();
		void handleAlignmentChange();
		void handleArrowStyleChange();
		void handleComponentLayoutChange();
		void handleComponentLayoutDirChange();
		void handleReactantVisibilityChange();
		void handleAgentVisibilityChange();
		void handleProductVisibilityChange();
		void handleAgentAlignmentChange();
		void handleAgentLayoutChange();
		void handleAgentLayoutDirChange();

		QLabel*                     statusMessageLabel;
		QLabel*                     viewInfoLabel;
		QFileDialog*                fileOpenDialog;
		QActionGroup*               windowListGroup;
		QMenu*                      contextMenu;
		QFileDialog*                fileSaveDialog;
		ChOX::Settings*             settings;
		ChOX::SettingsEditDialog*   settingsEditDialog;
		ChOX::DataSetViewControl*   dataSetViewControl;
		ChOX::DataSet*              dataSet;
		ChOX::DataSetView*          dataSetView;
		ChOX::RangeSelectionDialog* rangeSelectionDialog;
		Ui::MainWindow              uiMainWindow;
		std::vector<QAction*>       recentFilesMenuActions;
	};
}

#endif // CHOX_MAINWINDOW_HPP
