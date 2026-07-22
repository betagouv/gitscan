## Changelog : lab-anssi-ui-kit (30 derniers jours, au 21 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la bibliothèque, notamment des correctifs pour l'alignement des menus déroulants, des options de personnalisation pour les composants toggle et range, et une meilleure gestion des labels. Des efforts ont également été faits pour renforcer la sécurité du processus de CI/CD et améliorer l'organisation de la documentation.

### Évolutions fonctionnelles
- **DsfrDropdown:** Correction de l'alignement à droite du menu déroulant [#ee5eeed](https://github.com/betagouv/lab-anssi-ui-kit/pulls/ee5eeed).
- **DsfrToggle:** Ajout d'une propriété `hideLabel` pour masquer le label du toggle [#85ab8db](https://github.com/betagouv/lab-anssi-ui-kit/pulls/85ab8db). Correction de l'affichage de l'état "checked" [#2a15706](https://github.com/betagouv/lab-anssi-ui-kit/pulls/2a15706).
- **DsfrRange:** Ajout de la prise en charge de `box-sizing` [#baba2fe](https://github.com/betagouv/lab-anssi-ui-kit/pulls/baba2fe).
- **DsfrTabnav:** Ajout de la prise en charge de `createSlot` pour les liens du composant [#640145b](https://github.com/betagouv/lab-anssi-ui-kit/pulls/640145b).
- **DsfrLabel:** Ajout du composant `DsfrLabel` et remplacement de l'utilisation de la balise `<label>` par ce composant dans d'autres composants [#3230404](https://github.com/betagouv/lab-anssi-ui-kit/pulls/3230404, #4e3c862](https://github.com/betagouv/lab-anssi-ui-kit/pulls/4e3c862).
- **DsfrCheckboxesGroup & DsfrRadiosGroup:** Ajout de la prise en charge de la taille et de la graisse pour les légendes [#7e37811](https://github.com/betagouv/lab-anssi-ui-kit/pulls/7e37811).
- **DsfrLabel:** Ajout de la prise en charge de la taille et de la graisse [#9a1cd34](https://github.com/betagouv/lab-anssi-ui-kit/pulls/9a1cd34).
- **MarelLe:** Rendre les étapes plus slotable [#e8c5cf5](https://github.com/betagouv/lab-anssi-ui-kit/pulls/e8c5cf5).

### Évolutions techniques
- **CI/CD:** Ajout de `checkov` et `zizmor` pour valider la configuration de sécurité [#27897d5](https://github.com/betagouv/lab-anssi-ui-kit/pulls/27897d5). Désactivation des identifiants `git` des dépôts clonés et correction d'une injection potentielle [#df25557](https://github.com/betagouv/lab-anssi-ui-kit/pulls/df25557, #c048ebc](https://github.com/betagouv/lab-anssi-ui-kit/pulls/c048ebc).
- **Storybook:** Réorganisation des titres des composants Lab ANSSI et DSFR, suppression des options de tri des stories [#e177d4d](https://github.com/betagouv/lab-anssi-ui-kit/pulls/e177d4d, #cd06738](https://github.com/betagouv/lab-anssi-ui-kit/pulls/cd06738, #311dd6d](https://github.com/betagouv/lab-anssi-ui-kit/pulls/311dd6d).
- **DsfrSegmented:** Optimisation de `ResizeObserver` avec `requestAnimationFrame` [#4dab6e7](https://github.com/betagouv/lab-anssi-ui-kit/pulls/4dab6e7).
- **Renovate:** Ajout et mise à jour de la configuration renovate.json [#ccb1346](https://github.com/betagouv/lab-anssi-ui-kit/pulls/ccb1346, #df0ebdc](https://github.com/betagouv/lab-anssi-ui-kit/pulls/df0ebdc).

### Autres changements
- **Documentation:** Amélioration de l'organisation des stories d'exemples [#5df6d58](https://github.com/betagouv/lab-anssi-ui-kit/pulls/5df6d58).
- **Version:** Passage à la version 1.55.2, 1.55.1 et 1.55.0 [#104fad1](https://github.com/betagouv/lab-anssi-ui-kit/pulls/104fad1, #76da5b5](https://github.com/betagouv/lab-anssi-ui-kit/pulls/76da5b5, #6bb244f](https://github.com/betagouv/lab-anssi-ui-kit/pulls/6bb244f).
- **Figma:** Ajout de la configuration pour Code Connect [#48ac321](https://github.com/betagouv/lab-anssi-ui-kit/pulls/48ac321).
- **CI:** Mise à jour de l'étape de checkout pour utiliser la référence du dépôt et un fetch-depth de 0 [#c1c2325](https://github.com/betagouv/lab-anssi-ui-kit/pulls/c1c2325).
