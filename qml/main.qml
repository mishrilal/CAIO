import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15
import "controls"

Window {
    id: mainWindow
    width: 1000
    height: 580
    minimumWidth: 800
    minimumHeight: 500
    visible: true
    color: "#00000000"
    title: qsTr("CAIO")

    // Remove Title Bar
    flags: Qt.Window | Qt.FramelessWindowHint

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
        color: "#2c313c"
        border.color: "#383e4c"
        border.width: 1
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.rightMargin: windowMargin
        anchors.leftMargin: windowMargin
        anchors.topMargin: windowMargin
        anchors.bottomMargin: windowMargin
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
                color: "#1c1d20"
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
                    color: "#282c34"
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.bottom: parent.bottom
                    anchors.rightMargin: 0
                    anchors.leftMargin: 70
                    anchors.bottomMargin: 0

                    Label {
                        id: labelTopInfo
                        color: "#5f6a82"
                        text: qsTr("Application Description")
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
                        text: qsTr("| HOME")
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
                    height: 35
                    color: "#00000000"
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.top: parent.top
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
                        font.bold: false
                        font.family: "Verdana"
                        anchors.leftMargin: 5
                    }
                }

                Row {
                    id: rowBtns
                    x: 879
                    width: 105
                    height: 35
                    anchors.right: parent.right
                    anchors.top: parent.top
                    anchors.topMargin: 0
                    anchors.rightMargin: 0

                    TopBarButton{
                        id: btnMinimize
                        onClicked: {
                            mainWindow.showMinimized()
                            internal.restoreMargins()
                        }
                    }

                    TopBarButton {
                        id: btnMaximizeRestore
                        btnIconSource: "../images/svg_images/maximize_icon.svg"
                        onClicked: internal.maximizeRestore()
                    }

                    TopBarButton {
                        id: btnClose
                        btnColorClicked: "#ff007f"
                        btnIconSource: "../images/svg_images/close_icon.svg"
                        onClicked: mainWindow.close()
                    }
                }
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
                    color: "#1c1d20"
                    anchors.left: parent.left
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom
                    clip: true
                    anchors.leftMargin: 0
                    anchors.bottomMargin: 0
                    anchors.topMargin: 0

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
                                btnDashboard.isActiveMenu = true
                                btnView.isActiveMenu = false
                                btnAdd.isActiveMenu = false
                                btnRemove.isActiveMenu = false
                                btnSettings.isActiveMenu = false

                                pageDashboard.visible = true
                                pageView.visible = false
                                pageAdd.visible = false
                                pageRemove.visible = false
                                pageSettings.visible = false
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
                                btnDashboard.isActiveMenu = false
                                btnView.isActiveMenu = true
                                btnAdd.isActiveMenu = false
                                btnRemove.isActiveMenu = false
                                btnSettings.isActiveMenu = false

                                pageDashboard.visible = false
                                pageView.visible = true
                                pageAdd.visible = false
                                pageRemove.visible = false
                                pageSettings.visible = false
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
                                btnDashboard.isActiveMenu = false
                                btnView.isActiveMenu = false
                                btnAdd.isActiveMenu = true
                                btnRemove.isActiveMenu = false
                                btnSettings.isActiveMenu = false

                                pageDashboard.visible = false
                                pageView.visible = false
                                pageAdd.visible = true
                                pageRemove.visible = false
                                pageSettings.visible = false
                            }
                        }

                        LeftMenuBtn {
                            id: btnRemove
                            width: leftMenu.width
                            text: qsTr("Remove Faces")
                            btnIconSource: "../images/svg_images/remove_icon.svg"
                            isActiveMenu: false
                            onClicked: {
                                btnDashboard.isActiveMenu = false
                                btnView.isActiveMenu = false
                                btnAdd.isActiveMenu = false
                                btnRemove.isActiveMenu = true
                                btnSettings.isActiveMenu = false

                                pageDashboard.visible = false
                                pageView.visible = false
                                pageAdd.visible = false
                                pageRemove.visible = true
                                pageSettings.visible = false
                            }
                        }
                    }

                    LeftMenuBtn {
                        id: btnSettings
                        width: leftMenu.width
                        text: qsTr("Settings")
                        anchors.bottom: parent.bottom
                        anchors.bottomMargin: 25
                        btnIconSource: "../images/svg_images/settings_icon.svg"
                        isActiveMenu: false
                        onClicked: {
                            btnDashboard.isActiveMenu = false
                            btnView.isActiveMenu = false
                            btnAdd.isActiveMenu = false
                            btnRemove.isActiveMenu = false
                            btnSettings.isActiveMenu = true

                            pageDashboard.visible = false
                            pageView.visible = false
                            pageAdd.visible = false
                            pageRemove.visible = false
                            pageSettings.visible = true
                        }
                    }
                }


                Rectangle {
                    id: rectangle
                    height: 25
                    color: "#282c34"
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
                        color: "#5f6a82"
                        text: qsTr("Application Description")
                        anchors.left: parent.left
                        anchors.right: parent.right
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        verticalAlignment: Text.AlignVCenter
                        anchors.topMargin: 0
                        anchors.bottomMargin: 0
                        anchors.leftMargin: 8
                        anchors.rightMargin: 30
                    }
                }


                Rectangle {
                    id: contentPages
                    color: "#2c313c"
                    anchors.left: leftMenu.right
                    anchors.right: parent.right
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom
                    anchors.topMargin: 0
                    anchors.bottomMargin: 25
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
                        visible: true
                    }
                    Loader{
                        id: pageView
                        anchors.fill: parent
                        source: Qt.resolvedUrl("pages/viewPage.qml")
                        visible: false
                    }
                    Loader{
                        id: pageAdd
                        anchors.fill: parent
                        source: Qt.resolvedUrl("pages/addPage.qml")
                        visible: false
                    }
                    Loader{
                        id: pageRemove
                        anchors.fill: parent
                        source: Qt.resolvedUrl("pages/removePage.qml")
                        visible: false
                    }
                    Loader{
                        id: pageSettings
                        anchors.fill: parent
                        source: Qt.resolvedUrl("pages/settingsPage.qml")
                        visible: false
                    }

                }

                MouseArea {
                    id: resizeWindow
                    x: 884
                    y: 0
                    width: 25
                    height: 25
                    anchors.right: parent.right
                    anchors.bottom: parent.bottom
                    anchors.rightMargin: 0
                    anchors.bottomMargin: 0
                    cursorShape: Qt.SizeFDiagCursor

                    Image {
                        id: resizeImage
                        width: 16
                        height: 16
                        opacity: 0.5
                        anchors.fill: parent
                        source: "../images/svg_images/resize_icon.svg"
                        anchors.leftMargin: 5
                        anchors.topMargin: 5
                        sourceSize.height: 16
                        sourceSize.width: 16
                        fillMode: Image.PreserveAspectFit
                        antialiasing: false
                    }

                    DragHandler {
                        target: null
                        onActiveChanged: if(active){
                                             mainWindow.startSystemResize(Qt.RightEdge | Qt.BottomEdge)
                                         }
                    }

                }
            }
        }
    }

    DropShadow {
        anchors.fill: bg
        horizontalOffset: 0
        verticalOffset: 0
        radius: 10
        samples: 16
        color: "#80000000"
        source: bg
        z: 0
    }

    MouseArea {
        id: resizeLeft
        width: 10
        anchors.left: parent.left
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.leftMargin: 0
        anchors.bottomMargin: 10
        anchors.topMargin: 10
        cursorShape: Qt.SizeHorCursor

        DragHandler{
            target: null
            onActiveChanged: if(active) { mainWindow.startSystemResize(Qt.LeftEdge) }
        }
    }

    MouseArea {
        id: resizeRight
        width: 10
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.rightMargin: 0
        anchors.bottomMargin: 10
        anchors.topMargin: 10
        cursorShape: Qt.SizeHorCursor

        DragHandler{
            target: null
            onActiveChanged: if(active) { mainWindow.startSystemResize(Qt.RightEdge) }
        }
    }

    MouseArea {
        id: resizeBottom
        height: 10
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        anchors.leftMargin: 10
        anchors.rightMargin: 10
        anchors.bottomMargin: 0
        cursorShape: Qt.SizeVerCursor

        DragHandler{
            target: null
            onActiveChanged: if(active) { mainWindow.startSystemResize(Qt.BottomEdge) }
        }
    }

    MouseArea {
        id: resizeTop
        width: 0
        height: 10
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.leftMargin: 10
        anchors.rightMargin: 10
        anchors.topMargin: 0
        cursorShape: Qt.SizeVerCursor

        DragHandler{
            target: null
            onActiveChanged: if(active) { mainWindow.startSystemResize(Qt.TopEdge) }
        }
    }

}

/*##^##
Designer {
    D{i:0;formeditorZoom:0.66}
}
##^##*/
