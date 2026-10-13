## Changelog : rdv-insertion (30 derniers jours, au 08/10/2026)

### Résumé
Les récentes évolutions se sont concentrées sur l'amélioration de la fiabilité des données (gestion des numéros de téléphone, normalisation des identités) et sur la stabilisation des outils de suivi. Le service gagne en robustesse technique, notamment sur la gestion des statistiques et du monitoring, tout en enrichissant ses capacités d'interface via l'API.

### Évolutions fonctionnelles
- **Amélioration de la gestion des contacts** : Correction de la détection des codes pays pour les numéros mobiles des DROM ([#3397](https://github.com/gip-inclusion/rdv-insertion/issues/3397)).
- **Nouvelle capacité de recherche** : Ajout d'un point d'accès (endpoint) permettant de rechercher des utilisateurs de la plateforme de l'inclusion via l'API ([#3385](https://github.com/gip-inclusion/rdv-insertion/issues/3385)).
- **Fiabilisation des données utilisateurs** : 
    - Normalisation du NIR lors de l'assignation pour garantir l'unicité par département ([#3384](https://github.com/gip-inclusion/rdv-insertion/issues/3384)).
    - Optimisation de l'attribution des utilisateurs après enrichissement des données CNAF ([#3380](https://github.com/gip-inclusion/rdv-insertion/issues/3380)).
- **Corrections d'interface et de flux** :
    - Correction des liens de redirection dans les modales de confirmation ([#3381](https://github.com/gip-inclusion/rdv-insertion/issues/3381)).
    - Résolution d'un plantage de l'API lors de l'invitation d'utilisateurs sans catégorie de motif ([#3387](https://github.com/gip-inclusion/rdv-insertion/issues/3387)).

### Évolutions techniques
- **Optimisation de l'authentification** : Renforcement de l'usage du jeton OAuth de RDV-Solidarités ([#3375](https://github.com/gip-inclusion/rdv-insertion/issues/3375)) et amélioration de la gestion des transactions de jetons ([#3379](https://github.com/gip-inclusion/rdv-insertion/issues/3379)).
- **Stabilité du système et monitoring** :
    - Optimisation du calcul des statistiques pour prévenir les erreurs de mémoire dans les conteneurs ([#3382](https://github.com/gip-inclusion/rdv-insertion/issues/3382)).
    - Nettoyage important des alertes Sentry pour réduire le bruit (limites de taux, alertes métier non pertinentes, doublons par IP) ([#3389](https://github.com/gip-inclusion/rdv-insertion/issues/3389), [#3390](https://github.com/gip-inclusion/rdv-insertion/issues/3390), [#3383](https://github.com/gip-inclusion/rdv-insertion/issues/3383)).
- **Configuration des outils d'analyse** : Correction de la configuration de Matomo via les variables d'environnement ([#3393](https://github.com/gip-inclusion/rdv-insertion/issues/3393), [#3394](https://github.com/gip-inclusion/rdv-insertion/issues/3394)).

### Autres changements
- **Documentation** : Mise à jour de la documentation de l'API, du schéma de données et création d'un guide de conventions pour les agents ([#3392](https://github.com/gip-inclusion/rdv-insertion/issues/3392), [#3391](https://github.com/gip-inclusion/rdv-insertion/issues/3391), [#3386](https://github.com/gip-inclusion/rdv-insertion/issues/3386)).
- **Maintenance et conformité** : Ajout de la licence MIT ([#3401](https://github.com/gip-inclusion/rdv-insertion/issues/3401)) et intégration de CodeRabbit pour l'automatisation des revues de code ([#3402](https://github.com/gip-inclusion/rdv-insertion/issues/3402)).
