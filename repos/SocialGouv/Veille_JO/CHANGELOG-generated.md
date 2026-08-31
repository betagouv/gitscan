## Changelog : Veille_JO (30 derniers jours, au 10 août 2026)

### Résumé
Ce mois-ci, l'outil a gagné en autonomie grâce à l'automatisation de la publication des rapports de veille et en offrant une navigation plus fluide dans les archives. La précision de l'extraction des données réglementaires et la flexibilité de l'outil ont également été renforcées.

### Évolutions fonctionnelles
- **Amélioration de la consultation des archives** : ajout de filtres, optimisation de l'affichage et intégration d'un lien de retour vers la page d'accueil.
- **Précision des données extraites** : meilleure gestion des nouvelles unités dans les noms de médicaments, nettoyage des mots-clés et correction du traitement des titres dans les tableaux.
- **Flexibilité de saisie** : l'outil accepte désormais plusieurs formats de date pour les commandes, évitant ainsi les erreurs d'exécution.

### Évolutions techniques
- **Automatisation du déploiement** : mise en place d'une GitHub Action pour publier quotidiennement le rapport de veille sur GitHub Pages.
- **Optimisation du CI/CD** : 
    - Possibilité de spécifier une date précise pour le workflow de publication.
    - Amélioration de la robustesse des workflows pour éviter les alertes d'échec lorsque le Journal Officiel n'est pas encore publié.

### Autres changements
- **Documentation** : ajout des instructions d'installation pour macOS et réorganisation de la documentation de test dans le fichier `TESTS.md`.
