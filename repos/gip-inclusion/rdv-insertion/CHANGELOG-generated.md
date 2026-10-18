## Changelog : rdv-insertion (30 derniers jours, au 17 octobre 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur la fiabilisation des données (gestion des numéros de téléphone, identifiants NIR et logique des orientations) et sur l'amélioration de la stabilité du système. De nouvelles capacités de recherche ont été ajoutées via l'API, et les outils de suivi d'erreurs ont été optimisés pour réduire le bruit technique et améliorer la réactivité du support.

### Évolutions fonctionnelles
- Ajout d'un point de terminaison (endpoint) de recherche d'utilisateurs pour la plateforme de l'inclusion ([#3385](https://github.com/gip-inclusion/rdv-insertion/issues/3385)).
- Amélioration du suivi des dossiers : enregistrement de la date de clôture lors des modifications ([#3400](https://github.com/gip-inclusion/rdv-insertion/issues/3400)).
- Correction de la gestion des numéros de téléphone pour les départements d'outre-mer (DROM) ([#3397](https://github.com/gip-inclusion/rdv-insertion/issues/3397)).
- Optimisation de la logique des orientations (meilleure détection des chevauchements et gestion du statut d'activité) ([#3408](https://github.com/gip-inclusion/rdv-insertion/issues/3408)).
- Renforcement de l'intégrité des données utilisateurs via la normalisation du NIR lors de l'assignation ([#3384](https://github.com/gip-inclusion/rdv-insertion/issues/3384)).
- Stabilisation de l'API pour éviter les plantages lors de l'invitation d'utilisateurs sans catégorie de motif ([#3387](https://github.com/gip-inclusion/rdv-insertion/issues/3387)).

### Évolutions techniques
- **Gestion des erreurs et monitoring** : Optimisation de Sentry pour filtrer les alertes non pertinentes (limites de débit, alertes métier) ([#3389](https://github.com/gip-inclusion/rdv-insertion/issues/3389), [#3390](https://github.com/gip-inclusion/rdv-insertion/issues/3390), [#3383](https://github.com/gip-inclusion/rdv-insertion/issues/3383)) et amélioration de la gestion des jetons d'accès lors des interactions avec France Travail ([#3404](https://github.com/gip-inclusion/rdv-insertion/issues/3404)).
- **Stabilité et performance** : Sécurisation du calcul des statistiques pour prévenir les dépassements de mémoire dans les conteneurs ([#3382](https://github.com/gip-inclusion/rdv-insertion/issues/3382)) et correction de l'intégrité des contraintes de dépendance sur les tables d'agents ([#3407](https://github.com/gip-inclusion/rdv-insertion/issues/3407)).
- **Analytique** : Amélioration de la configuration de Matomo et de sa gestion via les variables d'environnement ([#3394](https://github.com/gip-inclusion/rdv-insertion/issues/3394), [#3393](https://github.com/gip-inclusion/rdv-insertion/issues/3393)).

### Autres changements
- **Documentation** : Mise à jour de la documentation de l'API ([#3386](https://github.com/gip-inclusion/rdv-insertion/issues/3386)), des schémas de données ([#3392](https://github.com/gip-inclusion/rdv-insertion/issues/3392)) et des conventions relatives aux agents ([#3391](https://github.com/gip-inclusion/rdv-insertion/issues/3391)).
- **Outils et conformité** : Ajout de la licence MIT ([#3401](https://github.com/gip-inclusion/rdv-insertion/issues/3401)) et configuration de l'outil de revue de code CodeRabbit ([#3402](https://github.com/gip-inclusion/rdv-insertion/issues/3402), [#3405](https://github.com/gip-inclusion/rdv-insertion/issues/3405)).
- **Tests** : Révision des cas de tests pour les évaluations ([#3403](https://github.com/gip-inclusion/rdv-insertion/issues/3403)).
