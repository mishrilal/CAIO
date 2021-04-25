import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15
import "controls"

ApplicationWindow {
    id: mainWindow
    width: 1000
    height: 580
    minimumWidth: 1000
    minimumHeight: 500
    visible: true
    color: "#00000000"
    title: qsTr("CAIO")

    // Remove Title Bar
//  flags: Qt.Window | Qt.FramelessWindowHint

    // Properties
    property int windowStatus: 0
    property int windowMargin: 10

    //Internal Functions
    QtObject{
        id: internal

        function resetResizeBorder() {
            //Resize visibility
            resizeLeft.visible = true
            resizeRight.visible = true
            resizeTop.visible = true
            resizeBottom.visible = true
        }

        function maximizeRestore() {
            if(windowStatus == 0){
                mainWindow.showMaximized()
                windowMargin = 0
                windowStatus = 1

                //Resize visibility
                resizeLeft.visible = false
                resizeRight.visible = false
                resizeTop.visible = false
                resizeBottom.visible = false
                btnMaximizeRestore.btnIconSource = "../images/svg_images/restore_icon.svg"
            } else {
                mainWindow.showNormal()
                windowStatus = 0
                windowMargin = 10

                //Reset visibility
                internal.resetResizeBorder()
                btnMaximizeRestore.btnIconSource = "../images/svg_images/maximize_icon.svg"
            }
        }

        function ifMaximizedWindowRestore() {
            if(windowStatus == 1){
                mainWindow.showNormal()
                windowStatus = 0
                windowMargin = 10

                //Reset visibility
                internal.resetResizeBorder()
                btnMaximizeRestore.btnIconSource = "../images/svg_images/maximize_icon.svg"
            }
        }

        function restoreMargins(){
            windowStatus = 0
            windowMargin = 10

            //Reset visibility
            internal.resetResizeBorder()
            btnMaximizeRestore.btnIconSource = "../images/svg_images/maximize_icon.svg"
        }
    }

    Rectangle {
        id: bg
        color: "#16181d"
        radius: 0
        border.color: "#383e4c"
        border.width: 1
        anchors.fill: parent
        z: 1

        Rectangle {
            id: appContainer
            color: "#00000000"
            anchors.fill: parent
            anchors.rightMargin: 1
            anchors.leftMargin: 1
            anchors.bottomMargin: 1
            anchors.topMargin: 1

            Rectangle {
                id: topBar
                height: 60
                color: "#0f1013"
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.rightMargin: 0
                anchors.leftMargin: 0
                anchors.topMargin: 0

                ToggleButton{
                    onClicked: animationMenu.running = true
                }

                Rectangle {
                    id: topBarDescription
                    y: 33
                    height: 25
                    color: "#0f1013"
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.bottom: parent.bottom
                    anchors.rightMargin: 0
                    anchors.leftMargin: 70
                    anchors.bottomMargin: 0

                    Label {
                        id: labelTopInfo
                        color: "#5f6a82"
                        anchors.left: parent.left
                        anchors.right: parent.right
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        verticalAlignment: Text.AlignVCenter
                        anchors.bottomMargin: 0
                        anchors.rightMargin: 302
                        anchors.leftMargin: 8
                        anchors.topMargin: 0
                    }

                    Label {
                        id: labelRightInfo
                        width: 300
                        color: "#5f6a82"
                        text: qsTr("")
                        anchors.left: labelTopInfo.right
                        anchors.right: parent.right
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        horizontalAlignment: Text.AlignRight
                        verticalAlignment: Text.AlignVCenter
                        anchors.rightMargin: 10
                        anchors.leftMargin: 0
                        anchors.bottomMargin: 0
                        anchors.topMargin: 0
                    }
                }

                Rectangle {
                    id: titleBar
                    color: "#00000000"
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.top: parent.top
                    anchors.bottom: topBarDescription.bottom
                    anchors.bottomMargin: 0
                    anchors.rightMargin: 105
                    anchors.leftMargin: 70
                    anchors.topMargin: 0

                    DragHandler{
                        onActiveChanged: if(active){
                                             mainWindow.startSystemMove()
                                             internal.ifMaximizedWindowRestore()
                                         }
                    }

                    Image {
                        id: iconApp
                        width: 22
                        height: 22
                        anchors.left: parent.left
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        source: "../images/svg_images/logo_Icon.svg"
                        autoTransform: true
                        anchors.leftMargin: 5
                        anchors.bottomMargin: 0
                        anchors.topMargin: 0
                        fillMode: Image.PreserveAspectFit
                    }

                    ColorOverlay{
                        anchors.fill: iconApp
                        source: iconApp
                        color: "#ffffff"
                    }


                    Label {
                        id: label
                        color: "#c3cbdd"
                        text: qsTr("CAIO")
                        anchors.left: iconApp.right
                        anchors.right: parent.right
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        horizontalAlignment: Text.AlignLeft
                        verticalAlignment: Text.AlignVCenter
                        font.pointSize: 21
                        font.bold: false
                        font.family: "Verdana"
                        anchors.leftMargin: 10
                    }

                }

                LockBtn{
                    id: btnLock
                    text: "START"
                    width: 120
                    anchors.right: parent.right
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom
                    anchors.rightMargin: 20
                    anchors.bottomMargin: 10
                    anchors.topMargin: 10

                    onClicked: {
                        backend.runLock()
                    }

                }

//                AboutButton {
//                    id: btnAbout
//                    anchors.verticalCenter: parent.verticalCenter
//                    anchors.right: parent.right
//                    anchors.verticalCenterOffset: 0
//                    anchors.rightMargin: 5
//                    onClicked: {
//                        pageDashboard.active = false
//                        pageView.active = false
//                        pageAdd.active = false
//                        pageRemove.active = false
//                        pageSettings.active = false
//                        pageAbout.active = true

//                        btnDashboard.isActiveMenu = false
//                        btnView.isActiveMenu = false
//                        btnAdd.isActiveMenu = false
//                        btnRemove.isActiveMenu = false
//                        btnSettings.isActiveMenu = false

//                        pageDashboard.visible = false
//                        pageView.visible = false
//                        pageAdd.visible = false
//                        pageRemove.visible = false
//                        pageSettings.visible = false
//                        pageAbout.visible = true
//                    }
//                }
            }

            Rectangle {
                id: content
                color: "#00000000"
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: topBar.bottom
                anchors.bottom: parent.bottom
                anchors.rightMargin: 0
                anchors.bottomMargin: 0
                anchors.leftMargin: 0
                anchors.topMargin: 0

                Rectangle {
                    id: leftMenu
                    width: 70
                    color: "#0f1013"
                    anchors.left: parent.left
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom
                    clip: true
                    anchors.leftMargin: 0
                    anchors.bottomMargin: 0
                    anchors.topMargin: 0

                    Label {
                        id: version
                        y: 457
                        height: 25
                        visible: false
                        color: "#ffffff"
                        text: qsTr("v0.0.65")
                        anchors.left: parent.left
                        anchors.right: parent.right
                        anchors.bottom: parent.bottom
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        wrapMode: Text.WordWrap
                        anchors.rightMargin: 0
                        anchors.leftMargin: 0
                        anchors.bottomMargin: 0
                    }

                    PropertyAnimation {
                        id: animationMenu
                        target: leftMenu
                        property: "width"
                        to: if(leftMenu.width == 70) return 180; else return 70
                        duration: 500
                        easing.type: Easing.OutBack
                    }

                    Column {
                        id: columnMenus
                        anchors.left: parent.left
                        anchors.right: parent.right
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        anchors.rightMargin: 0
                        anchors.leftMargin: 0
                        anchors.bottomMargin: 90
                        anchors.topMargin: 0

                        LeftMenuBtn {
                            id: btnDashboard
                            width: leftMenu.width
                            text: qsTr("Dashboard")
                            isActiveMenu: true
                            onClicked: {
                                pageDashboard.active = true
                                pageView.active = false
                                pageAdd.active = false
                                pageRemove.active = false
                                pageSettings.active = false
                                pageAbout.active = false
                                pageLog.active = false

                                btnDashboard.isActiveMenu = true
                                btnView.isActiveMenu = false
                                btnAdd.isActiveMenu = false
                                btnRemove.isActiveMenu = false
                                btnSettings.isActiveMenu = false
                                btnLogs.isActiveMenu = false
                                btnAbout.isActiveMenu = false

                                pageDashboard.visible = true
                                pageView.visible = false
                                pageAdd.visible = false
                                pageRemove.visible = false
                                pageSettings.visible = false
                                pageAbout.visible = false
                                pageLog.visible = false

                                backend.dashboardClicked()
                            }
                        }

                        LeftMenuBtn {
                            id: btnView
                            width: leftMenu.width
                            text: qsTr("View Faces")
                            iconWidth: 20
                            iconHeight: 20
                            btnIconSource: "../images/svg_images/view_icon.svg"
                            isActiveMenu: false
                            onClicked: {
                                pageDashboard.active = false
                                pageView.active = true
                                pageAdd.active = false
                                pageRemove.active = false
                                pageSettings.active = false
                                pageAbout.active = false
                                pageLog.active = false

                                btnDashboard.isActiveMenu = false
                                btnView.isActiveMenu = true
                                btnAdd.isActiveMenu = false
                                btnRemove.isActiveMenu = false
                                btnSettings.isActiveMenu = false
                                btnLogs.isActiveMenu = false
                                btnAbout.isActiveMenu = false

                                pageDashboard.visible = false
                                pageView.visible = true
                                pageAdd.visible = false
                                pageRemove.visible = false
                                pageSettings.visible = false
                                pageAbout.visible = false
                                pageLog.visible = false

                                backend.viewClicked()
                            }
                        }

                        LeftMenuBtn {
                            id: btnAdd
                            width: leftMenu.width
                            text: qsTr("Add Faces")
                            iconWidth: 18
                            iconHeight: 18
                            btnIconSource: "../images/svg_images/add_icon.svg"
                            isActiveMenu: false
                            onClicked: {
                                pageDashboard.active = false
                                pageView.active = false
                                pageAdd.active = true
                                pageRemove.active = false
                                pageSettings.active = false
                                pageAbout.active = false
                                pageLog.active = false

                                btnDashboard.isActiveMenu = false
                                btnView.isActiveMenu = false
                                btnAdd.isActiveMenu = true
                                btnRemove.isActiveMenu = false
                                btnSettings.isActiveMenu = false
                                btnLogs.isActiveMenu = false
                                btnAbout.isActiveMenu = false

                                pageDashboard.visible = false
                                pageView.visible = false
                                pageAdd.visible = true
                                pageRemove.visible = false
                                pageSettings.visible = false
                                pageAbout.visible = false
                                pageLog.visible = false

                                backend.addClicked()

                            }
                        }

                        LeftMenuBtn {
                            id: btnRemove
                            width: leftMenu.width
                            text: qsTr("Remove Faces")
                            btnIconSource: "../images/svg_images/remove_icon.svg"
                            isActiveMenu: false
                            onClicked: {
                                pageDashboard.active = false
                                pageView.active = false
                                pageAdd.active = false
                                pageRemove.active = true
                                pageSettings.active = false
                                pageAbout.active = false
                                pageLog.active = false

                                btnDashboard.isActiveMenu = false
                                btnView.isActiveMenu = false
                                btnAdd.isActiveMenu = false
                                btnRemove.isActiveMenu = true
                                btnSettings.isActiveMenu = false
                                btnLogs.isActiveMenu = false
                                btnAbout.isActiveMenu = false

                                pageDashboard.visible = false
                                pageView.visible = false
                                pageAdd.visible = false
                                pageRemove.visible = true
                                pageSettings.visible = false
                                pageAbout.visible = false
                                pageLog.visible = false

                                backend.removeClicked()

                            }
                        }
                        LeftMenuBtn {
                            id: btnLogs
                            width: leftMenu.width
                            visible: false
                            text: qsTr("Logs")
                            iconWidth: 20
                            iconHeight: 20
                            btnIconSource: "../images/svg_images/view_icon.svg"
                            isActiveMenu: false
                            onClicked: {
                                pageDashboard.active = false
                                pageView.active = false
                                pageAdd.active = false
                                pageRemove.active = false
                                pageSettings.active = false
                                pageAbout.active = false
                                pageLog.active = true

                                btnDashboard.isActiveMenu = false
                                btnView.isActiveMenu = false
                                btnAdd.isActiveMenu = false
                                btnRemove.isActiveMenu = false
                                btnSettings.isActiveMenu = false
                                btnLogs.isActiveMenu = true
                                btnAbout.isActiveMenu = false

                                pageDashboard.visible = false
                                pageView.visible = false
                                pageAdd.visible = false
                                pageRemove.visible = false
                                pageSettings.visible = false
                                pageAbout.visible = false
                                pageLog.visible = true

                                backend.allLogsClicked()
                            }
                        }
                    }

                    LeftMenuBtn {
                        id: btnAbout
                        width: leftMenu.width
                        text: qsTr("About Us")
                        anchors.bottom: btnSettings.top
                        anchors.bottomMargin: 0
                        btnIconSource: "../images/svg_images/about_icon.svg"
                        isActiveMenu: false
                        onClicked: {
                            pageDashboard.active = false
                            pageView.active = false
                            pageAdd.active = false
                            pageRemove.active = false
                            pageSettings.active = false
                            pageAbout.active = true

                            btnDashboard.isActiveMenu = false
                            btnView.isActiveMenu = false
                            btnAdd.isActiveMenu = false
                            btnRemove.isActiveMenu = false
                            btnSettings.isActiveMenu = false
                            btnAbout.isActiveMenu = true

                            pageDashboard.visible = false
                            pageView.visible = false
                            pageAdd.visible = false
                            pageRemove.visible = false
                            pageSettings.visible = false
                            pageAbout.visible = true
                        }
                    }

                    LeftMenuBtn {
                        id: btnSettings
                        width: leftMenu.width
                        text: qsTr("Preferences")
                        anchors.bottom: parent.bottom
                        anchors.bottomMargin: 0
                        btnIconSource: "../images/svg_images/settings_icon.svg"
                        isActiveMenu: false
                        onClicked: {
                            pageDashboard.active = false
                            pageView.active = false
                            pageAdd.active = false
                            pageRemove.active = false
                            pageSettings.active = true
                            pageAbout.active = false
                            pageLog.active = false

                            btnDashboard.isActiveMenu = false
                            btnView.isActiveMenu = false
                            btnAdd.isActiveMenu = false
                            btnRemove.isActiveMenu = false
                            btnSettings.isActiveMenu = true
                            btnLogs.isActiveMenu = false
                            btnAbout.isActiveMenu = false

                            pageDashboard.visible = false
                            pageView.visible = false
                            pageAdd.visible = false
                            pageRemove.visible = false
                            pageSettings.visible = true
                            pageAbout.visible = false
                            pageLog.visible = false

                            backend.settingsClicked()
                        }
                    }

                    Connections {
                        target: addFaceBackend;
                    }
                }


                Rectangle {
                    id: rectangle
                    height: 25
                    color: "#191c22"
                    anchors.left: leftMenu.right
                    anchors.right: parent.right
                    anchors.top: contentPages.bottom
                    anchors.bottom: parent.bottom
                    anchors.rightMargin: 0
                    anchors.leftMargin: 0
                    anchors.bottomMargin: 0
                    anchors.topMargin: 0

                    Label {
                        id: labelTopInfo1
                        visible: false
                        color: "#5e64e5"
                        text: qsTr("Developed By - THE PYTHONS")
                        anchors.left: parent.left
                        anchors.right: parent.right
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        horizontalAlignment: Text.AlignRight
                        verticalAlignment: Text.AlignVCenter
                        font.bold: true
                        anchors.leftMargin: 0
                        anchors.topMargin: 0
                        anchors.bottomMargin: 0
                        anchors.rightMargin: 2
                    }
                }


                Rectangle {
                    id: contentPages
                    color: "#00000000"
                    anchors.left: leftMenu.right
                    anchors.right: parent.right
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom
                    anchors.topMargin: 0
                    anchors.bottomMargin: 0
                    anchors.leftMargin: 0
                    anchors.rightMargin: 0

                    //                    StackView {
                    //                        id: stackView
                    //                        anchors.fill: parent
                    //                        clip: true
                    //                        initialItem: Qt.resolvedUrl("pages/dashboardPage.qml")
                    //                    }
                    Loader{
                        id: pageDashboard
                        anchors.fill: parent
                        source: Qt.resolvedUrl("pages/dashboardPage.qml")
                        active: true
                        visible: true
                    }
                    Loader{
                        id: pageView
                        anchors.fill: parent
                        source: Qt.resolvedUrl("pages/viewPage.qml")
                        active: false
                        visible: false
                    }
                    Loader{
                        id: pageAdd
                        anchors.fill: parent
                        source: Qt.resolvedUrl("pages/addPage.qml")
                        active: false
                        visible: false
                    }
                    Loader{
                        id: pageRemove
                        anchors.fill: parent
                        source: Qt.resolvedUrl("pages/removePage.qml")
                        active: false
                        visible: false
                    }
                    Loader{
                        id: pageSettings
                        anchors.fill: parent
                        source: Qt.resolvedUrl("pages/settingsPage.qml")
                        active: false
                        visible: false
                    }

                    Loader{
                        id: pageAbout
                        anchors.fill: parent
                        source: Qt.resolvedUrl("pages/aboutPage.qml")
                        active: false
                        visible: false
                    }
                    Loader{
                        id: pageLog
                        anchors.fill: parent
                        source: Qt.resolvedUrl("pages/logsPage.qml")
                        active: false
                        visible: false
                    }

                }

                
            }
        }
    }

    Connections {
        target: backend;

        function onSetLockBtn(value) {
            if(value === 1) {
//                print("Change to Red")
                btnLock.btnColorDefault = "#f44336"
                btnLock.btnColorMouseOver = "#ff7961"
                btnLock.btnColorClicked = "#ba000d"
                btnLock.text = "STOP"

            }
            else {
//                print("Change to Green")
                btnLock.btnColorDefault = "#1b5e20"
                btnLock.btnColorMouseOver = "#4c8c4a"
                btnLock.btnColorClicked = "#003300"
                btnLock.text = "START"
            }
        }
    }

}


