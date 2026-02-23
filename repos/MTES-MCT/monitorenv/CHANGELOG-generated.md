## Changelog : monitorenv (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à MonitorEnv au cours du dernier mois. Les principales évolutions concernent l'amélioration de la recherche de plages, l'ajout d'informations sur l'historique des navires, et une refonte technique importante de l'infrastructure et du pipeline de données pour une meilleure performance et maintenabilité.

### Évolutions fonctionnelles
- Ajout de l'historique des navires sur la page de résumé du navire (#af7c7c1).
- Affichage de la dernière position connue d'un navire sur la page de résumé (#e260f51).
- Amélioration de la recherche de plages, notamment en permettant la recherche sans accent (#db3962e, #3655ae8).
- Correction de l'affichage des zones réglementaires dans les briefs (#9c73b9d).
- Correction du filtre `controlPlan` dans la recherche de couches (#e716c08).

### Évolutions techniques
- Mise à jour de Poetry vers la version 3.6.9 (#9a6880d).
- Refonte importante de l'infrastructure et du pipeline de données : suppression de code legacy, mise à jour de la configuration, et simplification des workflows (#f5969b8, #cd8fe0c, #9845116, #503e2fe, #376dca2, #3036a5d, #2feb5eb, #03c91be, #4d5c3b9).
- Remplacement de la dépendance `cx_oracle` par `oracledb` (#2d2515f).
- Ajout de volumes pour les certificats Kafka (#95d038f).
- Utilisation de l'extension `unaccent` de PostgreSQL pour améliorer la recherche sans accent (#db3962e, #3655ae8).
- Mise à jour de Cypress (#de9eb8e).
- Mise à jour de Black (formatter de code Python) vers la version 26.1.0 (#96ab080).
- Mises à jour groupées de dépendances (non-major) (#c1805fb, #ad78352, #87f4632).
- Mise à jour de l'action `actions/setup-java` (#c3c6080).

### Autres changements
- Ajout de tests pour l'historique des navires (#f10770b).
- Correction d'un problème empêchant l'ouverture d'une fenêtre latérale lors des tests (#a32c9da).
- Correction d'un test (#bb39824).
- Mise à jour de la documentation Prefect 3 (#e69b967).
- Ajout d'un test manquant (#e258a56).
- Mise à jour de la configuration de Dependabot (#cd8fe0c).
- Ajout de la documentation pour l'installation du worker Prefect 3 (#e69b967).
- Suppression d'une requête inutilisée (#991ffe1).
- Mise à jour du fichier `CONTRIBUTING.md` (#9ee220e).
- Correction du flux de migration des données réglementaires (#0382dac).
- Correction du flux de données pour data.gouv (#7d69a79).
- Ajout de cache pour la recherche de couches (#fab1715).
- Refactorisation du hook `useSearchLayers` (#ca1f62b).
- Création du flow `ref_natinfs` (#d1230bd).
- Normalisation du chemin d'accès pour éviter les problèmes de superutilisateur (#5f6d74f).
- Correction d'un problème de type `jsonb` dans les modèles (#044566f).
- Mise à jour du hash de ligne pour les zones réglementaires (#b5016b6).
- Séparation du texte de recherche global de la requête d'entrée (#d885b99).
