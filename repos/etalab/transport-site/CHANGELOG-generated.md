## Changelog : transport-site (30 derniers jours, au 11 septembre 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur l'amélioration de la précision et de l'expérience utilisateur lors de la validation des données NeTEx. La plateforme a également bénéficié de renforcements de sécurité importants, d'une meilleure gestion des rapports pour les données IRVE et de diverses optimisations techniques visant à stabiliser le système et à réduire la duplication de code.

### Évolutions fonctionnelles
- **Validation NeTEx** : 
    - Amélioration de la visibilité des erreurs avec un tri par criticité décroissante [#5604] et l'affichage de la version XSD utilisée [#5607].
    - Meilleure gestion des versions via le choix automatique de la XSD selon la date de publication extraite des métadonnées [#5599, #5602, #5600].
    - Correction de l'affichage (layout) lorsque les données sont invalides [#5606].
- **Consolidation IRVE** : Ajout du statut des ressources dans les rapports de consolidation [#5565].
- **Données GBFS** : Correction du mapping pour les données Leo&Go [#5593].
- **Statistiques** : Extraction des données de téléchargement pour l'ART [#5590].

### Évolutions techniques
- **Sécurité** : Mise en œuvre du chiffrement des cookies [#5619] et application de mises à jour de sécurité globales [#5581].
- **Optimisation des performances** :
    - NeTEx : Passage au stockage direct en DataFrame pour la validation [#5577] et uniformisation du stockage/version du validateur [#5576].
    - IRVE : Optimisation du processus de correction des coordonnées en une seule passe [#5560].
- **Refactoring et Interface** :
    - Réduction de la duplication de code [#5618] et amélioration des layouts réutilisables [#5623].
    - Enrichissement de la bibliothèque de composants avec de nouvelles variantes pour les boutons colorés [#5603].
- **Maintenance et Infrastructure** :
    - Mise à jour du fichier `.proto` pour GTFS-RT [#5617].
    - Stabilisation des tests automatisés [#5587].
    - Correction de bugs de build (CSS minifié) [#5616] et résolution d'erreurs de monitoring Sentry [#5610].
