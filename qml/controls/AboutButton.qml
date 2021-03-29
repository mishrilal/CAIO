import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15

Button{
    id: btnAbout

    //Custom properties
    property url btnIconSource: "../../images/svg_images/about_icon.svg"
    property color btnColorDefault: "#5e64e5"
    property color btnColorMouseOver: "#767BF8"
    property color btnColorClicked: "#00a1f1"
    width: 30
    height: 30

    QtObject{
        id: internal

        // Mouse Hover and Click Change Color
        property var dynamicColor: if(btnAbout.down){
                                       btnAbout.down ? btnColorClicked : btnColorDefault
                                   } else {
                                       btnAbout.hovered ? btnColorMouseOver : btnColorDefault
                                   }
    }

    implicitWidth: 30
    implicitHeight: 30

    background: Rectangle{
        id: bgBtn
        color: "#00000000"
        //        color: internal.dynamicColor

        Image {
            id: iconBtn
            source: btnIconSource
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            height: 25
            width: 25
            fillMode: Image.PreserveAspectFit
        }

        ColorOverlay{
            anchors.fill: iconBtn
            source: iconBtn
            color: internal.dynamicColor
            antialiasing: false
        }
    }
}
