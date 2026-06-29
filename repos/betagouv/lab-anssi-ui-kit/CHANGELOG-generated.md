## Changelog : lab-anssi-ui-kit (30 derniers jours, au 25 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à plusieurs composants, notamment `DsfrDropdown`, `DsfrToggle`, `DsfrInput`, `DsfrAlert`, `DsfrTable` et `DsfrTile`, en ajoutant de nouvelles fonctionnalités et en corrigeant des problèmes d'affichage.  Des efforts ont également été faits pour améliorer la documentation et la gestion des événements des composants, ainsi que pour uniformiser la structure de certains éléments avec le Design System Français (DSFR).

### Évolutions fonctionnelles
- **DsfrDropdown :** Ajout d'une propriété `disabled` pour désactiver le bouton d'ouverture du menu déroulant et correction de l'alignement à droite du menu.
- **DsfrToggle :** Ajout de la propriété `hideLabel` pour masquer le label et correction de l'affichage de l'état "checked".
- **DsfrInput :** Ajout de variations "addon" (avec un bouton submit) et "action" (avec un bouton d'action) pour le champ de saisie. Refactoring du code du composant.
- **DsfrAlert :** Ajout de la propriété `titleTag` pour personnaliser la balise HTML du titre, amélioration de la logique d'affichage du titre et de la description en fonction de la taille.
- **DsfrTable :** Ajout de la gestion des lignes désactivées et d'une action pour gérer la propriété `--row-height`. Une story d'exemple de tableau avec lignes désactivées a été ajoutée.
- **DsfrTile :** Ajout de la propriété `noIcon` pour masquer l'icône associée au lien.
- **DsfrCheckbox :** Ajout de la gestion du style pour l'état disabled.
- **PresentationANSSI :** Uniformisation de la structure et du style avec les éléments du DSFR.

### Évolutions techniques
- **Gestion des événements :** Uniformisation de la façon de déclarer les `CustomEvent` et ajout des événements des composants à la table des arguments des stories Storybook. Les événements sont également ajoutés dans le fichier `web-types` généré.
- **Dépendances :** Mise à jour de la version des dépendances et épinglage des versions des dépendances des GitHub Actions pour plus de stabilité.
- **Storybook :** Ajout de la déclaration du dossier statique pour Storybook.
- **Types :** Ajout des types réels des props.
- **CI/CD :** Mise à jour de l'étape de checkout pour utiliser la référence du dépôt et un fetch-depth de 0.
- **Génération du fichier `web-types`:** Ajout d'un script pour générer un fichier `web-types` pour améliorer l'intégration avec les éditeurs de code.

### Autres changements
- **Documentation :** Amélioration de l'organisation des stories d'exemples.
- **Thèmes :** Ajout des couleurs hover et active pour le composant `DsfrTag` dans le thème MSC.
- **Correction :** Force la création du dossier `/dist` s'il n'existe pas.
- **Version :** Passage à la version 1.54.2, 1.54.1, 1.54.0 et 1.53.4.
