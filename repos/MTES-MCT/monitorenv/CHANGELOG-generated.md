## Changelog : monitorenv (30 derniers jours, au 27 août 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur l'amélioration de la gestion des zones réglementaires et la fiabilisation de l'interface utilisateur. Les utilisateurs bénéficieront d'outils de recherche plus précis et d'une saisie de données plus intuitive, tandis que la stabilité globale du système a été renforcée par une amélioration significative des tests automatisés.

### Évolutions fonctionnelles
- **Gestion des zones réglementaires** : introduction de groupes réglementaires avec de nouveaux formulaires, simplification de la saisie (tags désormais optionnels) et renforcement des contrôles (type et localisation obligatoires).
- **Recherche et navigation** : amélioration des capacités de recherche par localisation et affichage enrichi des options incluses dans les requêtes de recherche.
- **Expérience utilisateur (UX/UI)** : corrections ergonomiques sur les boutons et les sélecteurs d'arborescence, et résolution de problèmes d'affichage liés aux noms de couches et aux caractères spéciaux.
- **Précision des données** : correction de l'arrondi des coordonnées de longitude pour garantir la précision géographique.

### Évolutions techniques
- **Architecture et données** : restructuration des classes de données, optimisation des flux de données pour les zones réglementaires et gestion des migrations SQL.
- **Tests** : renforcement important de la suite de tests de bout en bout (E2E) pour assurer la stabilité des fonctionnalités de navigation et de couches.
- **Infrastructure et outils** : intégration de la clé API Carto et mise à jour de la syntaxe pour l'orchestrateur Prefect.

### Autres changements
- **Maintenance** : nettoyage du code et mise à jour des outils de formatage et de qualité (Prettier, Lint).
