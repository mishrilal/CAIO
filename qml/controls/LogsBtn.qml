import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15

Button{
    id: logBtn
    text: qsTr("All Logs")

    //Custom properties
    property url btnIconSource: "../../images/svg_images/dashboard_icon.svg"
    property color btnColorDefault: "#16181d"
    property color btnColorMouseOver: "#23272E"
    property color btnColorClicked: "#00a1f1"
    property int iconWidth: 18
    property int iconHeight: 18
    property color activeMenuColor: "#2c313c"
    property color activeMenuColorRight: "#55aaff"
    property bool isActiveMenu: false
    width: 150
    height: 50

    QtObject{
        id: internal

        // Mouse Hover and Click Change Color
        property var dynamicColor: if(logBtn.down){
                                       logBtn.down ? btnColorClicked : btnColorDefault
                                   } else {
                                       logBtn.hovered ? btnColorMouseOver : btnColorDefault
                                   }
    }

    implicitWidth: 150
    implicitHeight: 50

    background: Rectangle{
        id: bgBtn
        color: internal.dynamicColor

        Rectangle{
            anchors{
                top: parent.top
                left: parent.left
                bottom: parent.bottom
            }
            color: activeMenuColor
            width: 5
            visible: isActiveMenu
        }

        Rectangle{
            anchors{
                top: parent.top
                left: parent.left
                right: parent.right
            }
            color: activeMenuColor
            height: 5
            visible: isActiveMenu
        }

        Rectangle{
            anchors{
                top: parent.top
                right: parent.right
                bottom: parent.bottom
            }
            color: activeMenuColor
            width: 5
            visible: isActiveMenu
        }

        Rectangle{
            anchors{
                bottom: parent.bottom
                left: parent.left
                right: parent.right
            }
            color: activeMenuColor
            height: 5
            visible: !isActiveMenu
        }
    }

    contentItem: Item {
        anchors.fill: parent


//        Image {
//            id: iconBtn
//            source: btnIconSource
//            anchors.leftMargin: 26
//            anchors.verticalCenter: parent.verticalCenter
//            anchors.left: parent.left
//            sourceSize.width: iconWidth
//            sourceSize.height: iconHeight
//            width: iconWidth
//            height: iconHeight
//            fillMode: Image.PreserveAspectFit
//            visible: false
//            antialiasing: true
//        }

//        ColorOverlay{
//            anchors.fill: iconBtn
//            source: iconBtn
//            color: "#ffffff"
//            anchors.verticalCenter: parent.verticalCenter
//            antialiasing: true
//            width: iconWidth
//            height: iconHeight
//        }

        Rectangle{
            color: "#00000000"
            anchors.fill: parent
            anchors.rightMargin: 5
            anchors.leftMargin: 5
            anchors.bottomMargin: 5
            anchors.topMargin: 5

        }

        Text{
            color: "#ffffff"
            text: logBtn.text
            anchors.verticalCenter: parent.verticalCenter
            font: logBtn.font
            anchors.horizontalCenter: parent.horizontalCenter
        }
    }
}


