import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15
import "controls"

Window {
    id: splashScreen
    width: 550
    height: 400
    visible: true
    color: "#00000000"
    title: qsTr("CAIO")

    // Remove Title Bar
    flags: Qt.Window | Qt.FramelessWindowHint

    // Properties
    property int timeInterval: 300

    Timer{
        id: timer
        interval: timeInterval
        running: true
        repeat: false
        onTriggered: {
            var component = Qt.createComponent("main.qml")
            var win = component.createObject()
            win.show()
            visible = false
        }
    }

    Rectangle {
        id: bg
        radius: 20
        anchors.fill: parent
        gradient: Gradient {
            GradientStop {
                position: 0
                color: "#000000"
            }

            GradientStop {
                position: 0.5
                color: "#292727"
            }

            GradientStop {
                position: 1
                color: "#000000"
            }
        }

        Text {
             id: text1
             color: "#d5d5d5"
             text: qsTr("CAIO")
             elide: Text.ElideMiddle
             anchors.fill: parent
             font.letterSpacing: 5
             font.pixelSize: 48
             horizontalAlignment: Text.AlignHCenter
             verticalAlignment: Text.AlignVCenter
             styleColor: "#1238ba"
             font.family: "Times New Roman"
             font.italic: false
             font.underline: false
             font.bold: true
             minimumPixelSize: 12
         }
     }


}

/*##^##
Designer {
    D{i:0;formeditorZoom:0.75}
}
##^##*/
