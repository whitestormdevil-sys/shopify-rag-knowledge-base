---
source: https://polaris.shopify.com/components/selection-and-input/drop-zone
---

# Drop zone

The drop zone component lets users upload files by dragging and dropping the files into an area on a page, or activating a button.

### Upgrade to Polaris Web Components

Drop zone is now available as a framework-agnostic web component.

[Start using <s-drop-zone>](https://shopify.dev/docs/api/app-home/polaris-web-components/forms/dropzone)

### Drop zone component examples

DefaultWith a labelWith image file uploadWith single file uploadWith drop on pageAccepts only SVG filesNestedMedium-sizedSmall-sizedWith custom FileUpload textWith custom file dialog trigger

Use to allow merchants to upload files. They can drag and drop files into the dashed area, or upload traditionally by clicking the “Add file” button or anywhere inside the dashed area.

Edit in CodeSandbox

ReactHTML

```
import {DropZone, LegacyStack, Thumbnail, Text} from '@shopify/polaris';
import {NoteIcon} from '@shopify/polaris-icons';
import {useState, useCallback} from 'react';

function DropZoneExample() {
  const [files, setFiles] = useState<File[]>([]);

  const handleDropZoneDrop = useCallback(
    (_dropFiles: File[], acceptedFiles: File[], _rejectedFiles: File[]) =>
      setFiles((files) => [...files, ...acceptedFiles]),
    [],
  );

  const validImageTypes = ['image/gif', 'image/jpeg', 'image/png'];

  const fileUpload = !files.length && <DropZone.FileUpload />;
  const uploadedFiles = files.length > 0 && (
    <div style={{padding: '0'}}>
      <LegacyStack vertical>
        {files.map((file, index) => (
          <LegacyStack alignment="center" key={index}>
            <Thumbnail
              size="small"
              alt={file.name}
              source={
                validImageTypes.includes(file.type)
                  ? window.URL.createObjectURL(file)
                  : NoteIcon
              }
            />
            <div>
              {file.name}{' '}
              <Text variant="bodySm" as="p">
                {file.size} bytes
              </Text>
            </div>
          </LegacyStack>
        ))}
      </LegacyStack>
    </div>
  );

  return (
    <DropZone onDrop={handleDropZoneDrop}>
      {uploadedFiles}
      {fileUpload}
    </DropZone>
  );
}
```

## Props

interface DropZoneProps

label?React.ReactNode
:   Label for the file input.

labelAction?Action
:   Adds an action to the label.

labelHidden?boolean
:   Visually hide the label.

id?string
:   ID for file input.

accept?string
:   Allowed file types.

type?'file' | 'image' | 'video'
:   Whether is a file or an image.

    Defaults to 'file'.

active?boolean
:   Sets an active state.

error?boolean
:   Sets an error state.

outline?boolean
:   Displays an outline border.

    Defaults to true.

overlay?boolean
:   Displays an overlay on hover.

    Defaults to true.

overlayText?string
:   Text that appears in the overlay.

errorOverlayText?string
:   Text that appears in the overlay when set in error state.

allowMultiple?boolean
:   Allows multiple files to be uploaded at once.

    Defaults to true.

disabled?boolean
:   Sets a disabled state.

children?any
:   The child elements to render in the dropzone.

dropOnPage?boolean
:   Allows a file to be dropped anywhere on the page.

openFileDialog?boolean
:   Sets the default file dialog state.

variableHeight?boolean
:   Allows child content to adjust height.

customValidator?(file: File) => boolean
:   Adds custom validations.

onClick?(event: React.MouseEvent<HTMLElement>) => void
:   Callback triggered on click.

onDrop?(files: File[], acceptedFiles: File[], rejectedFiles: File[]) => void
:   Callback triggered on any file drop.

onDropAccepted?(acceptedFiles: File[]) => void
:   Callback triggered when at least one of the files dropped was accepted.

onDropRejected?(rejectedFiles: File[]) => void
:   Callback triggered when at least one of the files dropped was rejected.

onDragOver?() => void
:   Callback triggered when one or more files are dragging over the drag area.

onDragEnter?() => void
:   Callback triggered when one or more files entered the drag area.

onDragLeave?() => void
:   Callback triggered when one or more files left the drag area.

onFileDialogClose?() => void
:   Callback triggered when the file dialog is canceled.

## Best practices

### Drop zone

Drop zones should:

* Inform merchants when the file(s) can’t be uploaded:
  + When possible, use validation errors on drag to detect and explain things like file size limits or file types accepted.
  + Use the [banner component](https://polaris.shopify.com/components/feedback-indicators/banner) with a critical status to communicate errors that happen on the server.
* Provide feedback once the file(s) have been dropped and uploading begins.
* For convenience, allow files to be dropped anywhere on the page by enabling dropOnPage.
* Provide a file upload button to allow merchants to select files for upload in a traditional way. Do this by using the DropZone.FileUpload subcomponent.

### Validation errors

The drop zone component validates file type by default. File types you wish to accept can be defined by editing the accept property. This component also accepts custom validations using the customValidator property. When validation fails, the component sets itself to error mode.

---

## Content guidelines

### Client-side validation error messages

Client-side validation errors give instant feedback.

Validation error messages should be:

* Explicit: help merchants understand why their file can’t be uploaded and what they should change to successfully upload their file
* In sentence case: capitalize only the first word in the message
* Concise: use simple, clear language that can be read at a glance. For example:

File size must be less than 20MB

File type must be .gif, .jpg, .png or .svg

### Server-side upload error messages

Server-side upload errors give feedback after file submission.

Upload error messages should:

* Be displayed as a [banner](https://polaris.shopify.com/components/feedback-indicators/banner) with a critical status
* Show the name of the file(s) that were not uploaded successfully
* Describe why the file(s) couldn’t be uploaded and what merchants should change to upload their file successfully, as seen below

Example

```
The following images couldn’t be uploaded:

* “keep-it-real.png” is too large. Try a file size less than 20MB.
* “realer-than-real.zip” is not supported. File type must be .gif, .jpg, .png or .svg.
* “so-so-real.png” was interrupted due to weak network connection, [retry upload](#)
```

---

## Drop zone file upload

Use file upload with the drop zone component to let merchants select files for upload in a traditional way.

### File upload properties

| Prop | Type | Description | Default |
| --- | --- | --- | --- |
| actionTitle | string | String that appears in file upload | 'Add file' |
| actionHint | string | String that appears in file upload | 'or drop files to upload' |

---

## Related components

* To provide context to upload errors when they occur, use the [banner component](https://polaris.shopify.com/components/feedback-indicators/banner)
* To provide feedback during file upload, use the [spinner component](https://polaris.shopify.com/components/spinner)

---

## Accessibility

The drop zone component builds on the native HTML <input type="upload"> element. It includes a visual<button> as well as a drag and drop area that can receive keyboard focus.

### Keyboard support

To upload a file with the keyboard, merchants can interact with the drag-and-drop region.

* To give the input keyboard focus, use the `tab` key (or `shift` + `tab` when tabbing backwards)
* To activate the input, use the `enter`/`return` or `space` keys