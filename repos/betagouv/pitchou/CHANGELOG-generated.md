## Changelog : pitchou (30 derniers jours, au 17 octobre 2026)

### Résumé
Cette période a été marquée par l'amélioration des capacités d'exportation de données et une optimisation de l'ergonomie de l'interface, notamment pour la saisie des espèces. Des évolutions structurelles ont également été apportées à la gestion des porteurs de projet et au stockage des fichiers pour gagner en efficacité.

### Évolutions fonctionnelles
- **Export de données** : Possibilité d'exporter les dossiers filtrés aux formats CSV et ODS [#710](https://github.com/betagouv/pitchou/issues/710).
- **Gestion des dossiers** : Ajout de la gestion des décisions requises, de l'UICN et de la possibilité de supprimer des pièces jointes [#705](https://github.com/betagouv/pitchou/issues/705).
- **Authentification** : Autorisation de l'utilisation du domaine d'email `indre.gouv.fr`.
- **Interface utilisateur (UI/UX)** :
    - Mise en conformité responsive du layout de saisie des espèces [#706](https://github.com/betagouv/pitchou/issues/706).
    - Ajustements de la pagination, des onglets et des boutons d'action dans les dossiers [#707](https://github.com/betagouv/pitchou/issues/707).
    - Corrections diverses : clarification des imports de prescriptions et des conversions de surfaces [#714](https://github.com/betagouv/pitchou/issues/714), correction d'une coquille sur le label "perturbation" [#713](https://github.com/betagouv/pitchou/issues/713) et suppression de notifications redondantes sur les champs obligatoires [#711](https://github.com/betagouv/pitchou/issues/711).

### Évolutions techniques
- **Stockage** : Implémentation de l'upload direct vers S3 pour les fichiers [#704](https://github.com/betagouv/pitchou/issues/704).
- **Base de données** : Restructuration de l'entité "porteur de projet" [#709](https://github.com/betagouv/pitchou/issues/709).
- **Développement** : Ajout d'une option de capture d'email locale pour les environnements de développement [#715](https://github.com/betagouv/pitchou/issues/715).
