import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15

Button{
    id: btnLock
    text: qsTr("Lock")
    font.family: "Times New Roman"
    font.pointSize: 18

    //Custom properties
    property url btnIconSource: "../../images/svg_images/lock_icon.svg"
    property color btnColorDefault: "#1b5e20"
    property color btnColorMouseOver: "#4c8c4a"
    property color btnColorClicked: "#003300"
    property int iconWidth: 30
    property int iconHeight: 30
    property color activeMenuColor: "#55aaff"
    property color activeMenuColorRight: "#2c313c"
    property bool isActiveMenu: false
    width: 130
    height: 50

    QtObject{
        id: internal

        // Mouse Hover and Click Change Color
        property var dynamicColor: if(btnLock.down){
                                       btnLock.down ? btnColorClicked : btnColorDefault
                                   } else {
                                       btnLock.hovered ? btnColorMouseOver : btnColorDefault
                                   }
    }

    background: Rectangle{
        id: bgBtn
        color: internal.dynamicColor
        radius: 8
    }

    contentItem: Item {
        anchors.fill: parent
        id: content
        Image {
            id: iconBtn
            source: "../../images/svg_images/lock_icon.svg"
            anchors.leftMargin: 10
            anchors.verticalCenter: parent.verticalCenter
            anchors.left: parent.left
            sourceSize.width: iconWidth
            sourceSize.height: iconHeight
            width: iconWidth
            height: iconHeight
            fillMode: Image.PreserveAspectFit
            visible: false
            antialiasing: true
        }

        ColorOverlay{
            anchors.fill: iconBtn
            source: iconBtn
            color: "#000000"
            anchors.verticalCenter: parent.verticalCenter
            antialiasing: true
            width: iconWidth
            height: iconHeight
        }

        Text{
            color: "#000000"
            text: btnLock.text
            font: btnLock.font
            anchors.verticalCenter: parent.verticalCenter
            anchors.right: parent.right
            anchors.rightMargin: 15
        }
    }
}

/*##^##
Designer {
    D{i:0;autoSize:true;height:60;width:250}
}
##^##*/
