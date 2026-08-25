## Changelog : Veille_JO (30 derniers jours, au 10 août 2026)

### Résumé
Ce mois-ci, l'outil de veille a franchi une étape importante dans son automatisation et sa facilité d'utilisation. Les rapports de veille sont désormais publiés automatiquement chaque jour, et la consultation des archives a été grandement simplifiée. La précision de l'extraction des données médicales (unités, tableaux) a également été renforcée pour garantir une fiabilité accrue des rapports.

### Évolutions fonctionnelles
- **Amélioration de la consultation des archives** : ajout de filtres de recherche, optimisation de l'affichage des pages archivées et ajout d'un lien de retour vers l'accueil.
- **Précision des données extraites** : 
    - Meilleure gestion des nouvelles unités dans les noms de médicaments.
    - Nettoyage des mots-clés (suppression du terme "spécialité").
    - Correction de l'extraction des données pour éviter l'inclusion des titres dans les tableaux.
- **Flexibilité de saisie** : support de plusieurs formats de date pour les recherches, rendant l'outil plus tolérant aux erreurs de saisie.

### Évolutions techniques
- **Automatisation du déploiement** : mise en place d'une GitHub Action pour la publication quotidienne automatique des rapports de veille sur GitHub Pages.
- **Distribution simplifiée** : génération de binaires autonomes (via Nuitka) pour Windows, Linux et macOS, facilitant l'installation sans environnement Python complexe.
- **Robustesse de la CI/CD** : 
    - Optimisation des workflows pour éviter les alertes d'échec lorsque le Journal Officiel n'est pas encore publié.
    - Ajout de la possibilité de paramétrer la date de publication directement dans le workflow.

### Autres changements
- **Documentation** : 
    - Ajout des instructions d'installation spécifiques pour macOS.
    - Centralisation des procédures de tests dans un fichier `TESTS.md`.
    - Mise à jour de la présentation du projet.
