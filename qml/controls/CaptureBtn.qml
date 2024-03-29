import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15

Button{
    id: captureBtn
    text: qsTr("Capture")
    font.pointSize: 18

    //Custom properties
    property url btnIconSource: "../../images/svg_images/capture_icon.svg"
    property color btnColorDefault: "#5e64e5"
    property color btnColorMouseOver: "#767BF8"
    property color btnColorClicked: "#00a1f1"
    property int iconWidth: 18
    property int iconHeight: 18
    property bool isActiveMenu: false
    width: 170

    QtObject{
        id: internal

        // Mouse Hover and Click Change Color
        property var dynamicColor: if(captureBtn.down){
                                       captureBtn.down ? btnColorClicked : btnColorDefault
                                   } else {
                                       captureBtn.hovered ? btnColorMouseOver : btnColorDefault
                                   }
    }

    implicitWidth: 250
    implicitHeight: 60

    background: Rectangle{
        id: bgBtn
        color: internal.dynamicColor
        radius: 10
    }

    contentItem: Item {
        anchors.fill: parent
        id: content
        Image {
            id: iconBtn
            source: btnIconSource
            anchors.leftMargin: 26
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
            color: "#7f5fac"
            anchors.verticalCenter: parent.verticalCenter
            antialiasing: true
            width: iconWidth
            height: iconHeight
        }

        Text{
            color: "#a184cb"
            text: "Capture"
            font: captureBtn.font
            anchors.verticalCenter: parent.verticalCenter
            anchors.left: parent.left
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            minimumPointSize: 6
            font.pointSize: 21
            font.family: "Times New Roman"
            minimumPixelSize: 10
            anchors.leftMargin: 75
        }
    }

    onClicked: {
        addFaceBackend.captureClicked()
        camera.imageCapture.capture();
    }
}


