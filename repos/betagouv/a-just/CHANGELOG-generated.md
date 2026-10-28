## Changelog : a-just (30 derniers jours, au 27 octobre 2026)

### Résumé
Ce mois a été marqué par un renforcement des fonctionnalités de gestion des ressources humaines, notamment sur le suivi des activités et des remplacements (backups). L'expérience utilisateur a été affinée grâce à des améliorations de l'interface et de la saisie de données, tandis qu'un effort majeur de stabilisation a été réalisé via la correction et l'extension des tests automatisés pour garantir la fiabilité des parcours critiques.

### Évolutions fonctionnelles
- **Gestion des RH et activités** : Amélioration de la gestion des activités et des remplacements, incluant de nouveaux filtres et une meilleure intégration des données de remplacement.
- **Extraction de données** : Ajout de la possibilité de saisir manuellement la date pour l'extracteur des données d'activité.
- **Interface utilisateur** :
    - Optimisation du menu des juridictions pour afficher les options de remplacement en fonction de leur disponibilité.
    - Modernisation du formulaire d'inscription avec l'intégration d'un composant d'autocomplétion pour une saisie plus fluide et cohérente.
    - Amélioration de la lisibilité des libellés (groupes, arrondissements) et ajustements textuels pour une meilleure clarté.
- **Corrections** : Résolution d'un bug lors de l'exportation des fiches individuelles.

### Évolutions techniques
- **Stabilité et Qualité** : Travail intensif de maintenance et de correction des tests de bout en bout (E2E) pour sécuriser les fonctionnalités clés (connexion, ajout d'agent, tableaux de bord panorama et cockpit, accès).
- **Performance et Gestion des données** :
    - Implémentation d'un système de cache pour les activités du mois précédent afin d'optimiser les temps de réponse.
    - Introduction de la gestion de la visibilité des référentiels.
    - Amélioration de la gestion de la concurrence et des mises à jour par lots (batch updates) pour les données référentielles.
- **Sécurité et Accès** : Refactorisation de la logique de contrôle d'accès pour les ressources humaines et simplification de la gestion des droits de modification (mode lecture seule) dans les formulaires.

### Autres changements
- Mise à jour de la version vers la v3.7.2.
- Ajustements cosmétiques (couleurs, espacements et styles) pour renforcer la cohérence visuelle de l'application.
