## Changelog : ecopass (30 derniers jours, au 28 août 2026)

### Résumé
Ce mois-ci, la plateforme a considérablement évolué pour offrir une gestion plus fine des utilisateurs et des données. L'introduction d'un profil "citoyen", l'amélioration de la gestion des organisations et le renforcement des contrôles de sécurité permettent une utilisation plus structurée. Parallèlement, la précision des informations produits a été enrichie (URL, catégories, niveaux de confiance) et la robustesse du système a été consolidée par l'ajout de nouveaux tests automatisés.

### Évolutions fonctionnelles
- **Gestion des utilisateurs et accès** :
    - Création du profil "citoyen" [#197](https://github.com/incubateur-ademe/ecopass/issues/197).
    - Mise en place de la gestion des membres au sein d'une organisation [#191](https://github.com/incubateur-ademe/ecopass/issues/191).
    - Ajout de la possibilité de s'inscrire directement via la page de connexion publique [#196](https://github.com/incubateur-ademe/ecopass/issues/196).
    - Renforcement de la sécurité par la restriction des actions pour les profils "lecteurs" [#195](https://github.com/incubateur-ademe/ecopass/issues/195) et la limitation de l'accès aux déclarations récentes [#192](https://github.com/incubateur-ademe/ecopass/issues/192).
- **Gestion et données produits** :
    - Enrichissement des données produits avec l'ajout d'URL [#201](https://github.com/incubateur-ademe/ecopass/issues/201) et de sélecteurs de catégories [#198](https://github.com/incubateur-ademe/ecopass/issues/198).
    - Amélioration de la précision des données via le calcul du score moyen [#189](https://github.com/incubateur-ademe/ecopass/issues/189) et l'ajout d'un niveau de confiance [#187](https://github.com/incubateur-ademe/ecopass/issues/187).
    - Introduction d'une première version de déclaration simplifiée [#185](https://github.com/incubateur-ademe/ecopass/issues/185).
    - Corrections et contraintes : correction de la recherche de produits [#190](https://github.com/incubateur-ademe/ecopass/issues/190), limitation de la masse lors des téléchargements [#188](https://github.com/incubateur-ademe/ecopass/issues/188) et gestion des redirections [#186](https://github.com/incubateur-ademe/ecopass/issues/186).

### Évolutions techniques
- **Automatisation et infrastructure** :
    - Implémentation d'une tâche planifiée (cron) pour la gestion des envois d'emails [#193](https://github.com/incubateur-ademe/ecopass/issues/193) et correction de la commande cron associée.
- **Qualité et tests** :
    - Renforcement de la fiabilité du code avec l'ajout de tests unitaires [#200](https://github.com/incubateur-ademe/ecopass/issues/200) et de tests de bout en bout (E2E) [#199](https://github.com/incubateur-ademe/ecopass/issues/199).
