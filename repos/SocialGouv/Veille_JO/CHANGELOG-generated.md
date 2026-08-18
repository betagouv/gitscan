## Changelog : Veille_JO (30 derniers jours, au 10 août 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape clé dans l'automatisation de la diffusion de ses rapports. L'accent a été mis sur l'amélioration de la consultation des archives et la robustesse de l'extraction des données réglementaires, tout en automatisant la publication quotidienne des rapports de veille pour une accessibilité accrue.

### Évolutions fonctionnelles
- **Amélioration de la consultation des archives** : ajout de filtres de recherche et d'une navigation simplifiée (lien de retour à l'accueil).
- **Précision des données extraites** : prise en compte de nouvelles unités pour les noms de médicaments et nettoyage des mots-clés pour éviter les erreurs de filtrage.
- **Flexibilité de l'outil** : l'argument `--date` accepte désormais plusieurs formats, rendant l'outil plus souple lors de l'exécution manuelle.
- **Correction d'affichage** : résolution d'un problème d'interprétation des titres dans les tableaux de données.

### Évolutions techniques
- **Automatisation du déploiement** : mise en place d'une GitHub Action pour la publication automatique et quotidienne du rapport de veille sur GitHub Pages.
- **Distribution simplifiée** : automatisation de la création de binaires autonomes (via Nuitka) pour Windows, Linux et macOS.
- **Fiabilisation des workflows CI/CD** : 
    - Gestion des cas où le Journal Officiel n'est pas encore publié pour éviter les alertes d'échec inutiles.
    - Possibilité de spécifier une date précise pour le workflow de publication des pages.

### Autres changements
- **Documentation** : ajout d'instructions d'installation pour macOS et centralisation des procédures de tests dans un fichier dédié (`TESTS.md`).
- **Supports** : mise à jour de la présentation de l'outil.
