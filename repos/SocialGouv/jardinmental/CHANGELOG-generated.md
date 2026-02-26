## Changelog : jardinmental (30 derniers jours)

### Résumé
Ce mois-ci, l'application Jardin Mental a bénéficié d'améliorations de la documentation, de corrections de bugs concernant l'affichage et le fonctionnement de certains écrans (sondages, outils de cohérence cardiaque), et d'une migration vers l'outil de gestion de paquets pnpm pour optimiser le processus de construction et de déploiement. Des ajustements ont également été apportés à l'interface utilisateur pour une meilleure expérience.

### Évolutions fonctionnelles
- Amélioration de l'affichage du panneau inférieur pour l'outil de cohérence cardiaque, permettant de le fermer par un geste de glissement.
- Correction d'un bug empêchant l'ouverture correcte du sondage en cas de données manquantes.
- Correction d'un problème d'affichage du label flottant dans les champs de saisie, qui était masqué par la bordure.
- Modification du titre de retour de l'écran "Outil".
- Ajout d'informations spécifiques pour le CHU Anger dans l'écran "ComityScreen".
- Correction de l'affichage du texte dans le contexte des notes.

### Évolutions techniques
- Migration du build et des workflows CI/CD vers l'utilisation de pnpm, remplaçant `npx`.
- Ajout de la configuration Babel et Jest pour les tests.
- Ajout d'un fichier `.npmrc`.
- Mise à jour de la configuration de Jest.
- Ajout d'un script pour générer les fichiers Prisma après la construction.

### Autres changements
- Mise à jour de la documentation README avec des informations sur l'ajout de données de ressources, les instructions pour se connecter à l'API Docker avec k9s, et des précisions sur le processus de build.
- Modification de l'adresse email utilisée pour les notifications.
- Augmentation des numéros de version pour iOS et Android.
- Ajout d'informations sur les propriétés des outils dans la documentation.
- Correction de références à des fichiers inexistants dans le README.
- Suppression d'un lien inutile dans le README.
