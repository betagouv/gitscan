## Changelog : jardinmental (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe de développement s'est concentrée sur l'amélioration de l'expérience utilisateur, notamment en corrigeant des bugs d'affichage et en optimisant l'interface. Des efforts ont également été déployés pour moderniser l'infrastructure de build et améliorer la documentation du projet.

### Évolutions fonctionnelles
- Amélioration de l'affichage des feuilles de fond (bottom sheets) pour l'outil de cohérence cardiaque.
- Correction d'un bug empêchant l'ouverture correcte du questionnaire quotidien sans données.
- Correction d'un problème d'affichage du label flottant dans les champs de texte.
- Ajout de la possibilité de fermer les feuilles de fond en effectuant un geste de glissement vers le bas.
- Modification du titre de retour de l'écran "Outil".
- Ajout d'informations spécifiques pour le centre de gestion des situations (CHU Anger) dans l'écran "ComityScreen".

### Évolutions techniques
- Passage à l'utilisation de `pnpm` pour la gestion des paquets et le build du projet, améliorant potentiellement la performance et la cohérence.
- Mise à jour de la configuration de Babel et Jest pour une meilleure compatibilité et des tests plus fiables.
- Ajout d'un fichier `.npmrc` pour configurer plus finement `pnpm`.
- Modification de la configuration des workflows CI/CD pour utiliser `pnpm`.
- Ajout d'un script pour générer les fichiers Prisma après le build.

### Autres changements
- Mise à jour de la documentation README avec des informations supplémentaires sur la configuration, le build et l'ajout de données de ressources.
- Modification de l'adresse e-mail utilisée pour les notifications (passage de Fabrique à CNAM).
- Augmentation des numéros de version Android et iOS.
- Ajout d'instructions pour se connecter à l'API Docker avec k9s.
- Ajout d'informations sur les hooks de configuration en mode développement pour le graphique de corrélation et le navigateur intégré.
- Correction de l'affichage d'un texte barré dans un champ de saisie.
- Correction de l'affichage d'une note contextuelle.
- Correction de l'alignement d'une icône.
- Ajout d'informations sur le workflow d'ajout de données de ressources.
