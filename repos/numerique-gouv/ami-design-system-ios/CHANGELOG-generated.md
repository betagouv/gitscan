## Changelog : ami-design-system-ios (30 derniers jours, au 21 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'enrichissement de la bibliothèque de composants avec l'ajout de nouveaux éléments comme la galerie de boutons et la vue "Tile". Des efforts ont également été faits pour améliorer l'intégration et la configuration des couleurs du design system, notamment en adoptant la couleur d'accent par défaut du DSFR. Plusieurs corrections et refactorings ont été effectués pour améliorer la structure du projet et faciliter son utilisation.

### Évolutions fonctionnelles
- Ajout d'une galerie de boutons avec différentes tailles et styles [#f08cbb5](https://github.com/numerique-gouv/ami-design-system-ios/commit/f08cbb5)
- Création d'un nouveau composant "TileView" pour afficher des informations structurées [#78cbaa9](https://github.com/numerique-gouv/ami-design-system-ios/commit/78cbaa9)
- Amélioration de la vue "Pills" avec la migration des types [#13d9bd6](https://github.com/numerique-gouv/ami-design-system-ios/commit/13d9bd6)
- Amélioration de l'alignement et du comportement du texte dans la vue "TileView" pour permettre le multiligne et l'alignement à gauche [#64de0ea](https://github.com/numerique-gouv/ami-design-system-ios/commit/64de0ea)

### Évolutions techniques
- Définition de la couleur d'accent par défaut du DSFR pour SwiftUI et UIKit [#e0d61e5](https://github.com/numerique-gouv/ami-design-system-ios/commit/e0d61e5)
- Déplacement du composant "Button" DSFR dans le "Design System" pour une meilleure organisation [#6c65c74](https://github.com/numerique-gouv/ami-design-system-ios/commit/6c65c74)
- Refactoring de la structure du projet avec le déplacement des ressources et du code Swift dans un sous-dossier "DesignSystem" [#78cbaa9](https://github.com/numerique-gouv/ami-design-system-ios/commit/78cbaa9)
- Modification de la structure du package Swift pour faciliter son intégration dans d'autres projets via l'URL GitHub [#8042719](https://github.com/numerique-gouv/ami-design-system-ios/commit/8042719)
- Rendre les composants publics pour une utilisation plus aisée [#438ef5e](https://github.com/numerique-gouv/ami-design-system-ios/commit/438ef5e) et [#65e8756](https://github.com/numerique-gouv/ami-design-system-ios/commit/65e8756)
- Définition des propriétés de style du bouton (police, taille, couleur, rayon de bordure, padding) comme propriétés de classe [#4ce9677](https://github.com/numerique-gouv/ami-design-system-ios/commit/4ce9677), [#c018330](https://github.com/numerique-gouv/ami-design-system-ios/commit/c018330), [#5a40159](https://github.com/numerique-gouv/ami-design-system-ios/commit/5a40159), [#3574715](https://github.com/numerique-gouv/ami-design-system-ios/commit/3574715)
- Chargement des polices depuis le module [#4ce9677](https://github.com/numerique-gouv/ami-design-system-ios/commit/4ce9677)

### Autres changements
- Mise à jour de la documentation (Readme) concernant la couleur d'accent par défaut du DSFR [#62d445e](https://github.com/numerique-gouv/ami-design-system-ios/commit/62d445e)
- Correction de l'accès aux composants DSFR depuis l'application d'exemple [#8bb27d3](https://github.com/numerique-gouv/ami-design-system-ios/commit/8bb27d3)
- Suppression de code inutilisé [#4929ea9](https://github.com/numerique-gouv/ami-design-system-ios/commit/4929ea9) et de fichiers de ressources inutilisés [#f5d5486](https://github.com/numerique-gouv/ami-design-system-ios/commit/f5d5486)
- Correction de problèmes de linter [#936815c](https://github.com/numerique-gouv/ami-design-system-ios/commit/936815c)
- Mise à jour du script de génération du projet d'exemple et du Readme [#b68f40b](https://github.com/numerique-gouv/ami-design-system-ios/commit/b68f40b)
- Correction du descripteur de build [#dc356f4](https://github.com/numerique-gouv/ami-design-system-ios/commit/dc356f4)
