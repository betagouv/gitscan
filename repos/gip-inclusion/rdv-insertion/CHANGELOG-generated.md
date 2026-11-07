## Changelog : rdv-insertion (30 derniers jours, au 06/11/2026)

### Résumé
Ce mois-ci, les développements se sont concentrés sur le renforcement de la sécurité de la plateforme, l'amélioration de la fiabilité des échanges de données avec France Travail et l'optimisation des processus de revue de code automatisés pour garantir une meilleure qualité logicielle.

### Évolutions fonctionnelles
- **Intégration France Travail** : Amélioration de la précision des données échangées, notamment sur l'envoi du libellé d'adresse et la lecture des catégories de motifs dans les suivis [#3421](https://github.com/gip-inclusion/rdv-insertion/issues/3421), [#3420](https://github.com/gip-inclusion/rdv-insertion/issues/3420) et une meilleure gestion des erreurs de réponse [#3404](https://github.com/gip-inclusion/rdv-insertion/issues/3404).
- **Gestion des orientations** : Optimisation du calcul des orientations actives et détection des chevauchements horaires [#3408](https://github.com/gip-inclusion/rdv-insertion/issues/3408).
- **Suivi des dossiers** : Possibilité d'enregistrer la date de clôture d'un suivi lors de ses modifications [#3400](https://github.com/gip-inclusion/rdv-insertion/issues/3400).
- **API & Interface** : Exposition du type de catégorie de motif via l'API [#3411](https://github.com/gip-inclusion/rdv-insertion/issues/3411) et mise à jour des textes de la page d'accueil [#3425](https://github.com/gip-inclusion/rdv-insertion/issues/3425).

### Évolutions techniques
- **Sécurité** : Renforcement de la recherche d'utilisateurs sur la plateforme [#3429](https://github.com/gip-inclusion/rdv-insertion/issues/3429), mise en place d'un limitation de débit (rate limiting) basée sur le NIR plutôt que sur l'IP [#3409](https://github.com/gip-inclusion/rdv-insertion/issues/3409) et sécurisation des webhooks Brevo [#3428](https://github.com/gip-inclusion/rdv-insertion/issues/3428).
- **Maintenance et sécurité des dépendances** : Mises à jour critiques pour corriger des vulnérabilités ou améliorer la stabilité (Rails [#3426](https://github.com/gip-inclusion/rdv-insertion/issues/3426), Rack [#3419](https://github.com/gip-inclusion/rdv-insertion/issues/3419), Dompurify [#3414](https://github.com/gip-inclusion/rdv-insertion/issues/3414)) et montée de version de Ruby [#3416](https://github.com/gip-inclusion/rdv-insertion/issues/3416).
- **CI/CD & Revue de code** : Optimisation du processus de revue automatisée avec l'intégration et le paramétrage de l'outil "relecteur" [#3410](https://github.com/gip-inclusion/rdv-insertion/issues/3410), [#3417](https://github.com/gip-inclusion/rdv-insertion/issues/3417) et ajustements de la configuration CodeRabbit [#3402](https://github.com/gip-inclusion/rdv-insertion/issues/3402), [#3405](https://github.com/gip-inclusion/rdv-insertion/issues/3405), [#3424](https://github.com/gip-inclusion/rdv-insertion/issues/3424).
- **Base de données** : Correction de dépendances manquantes sur les tables liées aux agents [#3407](https://github.com/gip-inclusion/rdv-insertion/issues/3407).

### Autres changements
- **Légal** : Ajout de la licence MIT au projet [#3401](https://github.com/gip-inclusion/rdv-insertion/issues/3401).
- **Tests** : Révision des cas de tests négatifs pour les évaluations [#3403](https://github.com/gip-inclusion/rdv-insertion/issues/3403).
