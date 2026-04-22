## Changelog : OTP-DS-to-Grist (30 derniers jours, au 21 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la robustesse de la synchronisation des données, notamment la gestion des dates et des erreurs. Des correctifs ont été apportés pour améliorer la précision des messages d'erreur et la gestion du chargement des données. La documentation a également été mise à jour avec un nouveau README pour le dossier de synchronisation. Enfin, plusieurs dépendances ont été mises à jour pour bénéficier des dernières corrections et améliorations de sécurité.

### Évolutions fonctionnelles
- Amélioration de la conversion des dates : la conversion de la colonne `updated_since_cursor` vers une chaîne de caractères est maintenant gérée correctement lorsque la colonne Grist est de type Date. [#283](https://github.com/betagouv/OTP-DS-to-Grist/issues/283)
- Ajout de données de 2 nouvelles tables : la synchronisation a été étendue pour inclure les données de deux tables supplémentaires. [#278](https://github.com/betagouv/OTP-DS-to-Grist/issues/278)
- Amélioration de la précision des erreurs : les messages d'erreur affichés lors des synchronisations automatiques sont plus précis, facilitant le diagnostic des problèmes. [#276](https://github.com/betagouv/OTP-DS-to-Grist/issues/276)
- Amélioration du loader : le loader a été optimisé pour une meilleure précision et une meilleure gestion des erreurs. [#270](https://github.com/betagouv/OTP-DS-to-Grist/issues/270) et [#249](https://github.com/betagouv/OTP-DS-to-Grist/issues/249)
- Ajout de la récupération et de la création de la table "expert" [#247](https://github.com/betagouv/OTP-DS-to-Grist/issues/247) et [#248](https://github.com/betagouv/OTP-DS-to-Grist/issues/248)

### Évolutions techniques
- Documentation : Ajout d'un nouveau README pour le dossier `sync`, améliorant la documentation du projet. [#282](https://github.com/betagouv/OTP-DS-to-Grist/issues/282)
- Optimisation des performances : optimisation de la récupération des données, incluant la mise en cache globale, l'utilisation d'instructeurs uniques et le traitement par lots des champs. [#224](https://github.com/betagouv/OTP-DS-to-Grist/issues/224)
- Suppression de code mort et ajout de fallbacks pour une meilleure robustesse. [#257](https://github.com/betagouv/OTP-DS-to-Grist/issues/257)
- Suppression des crochets et guillemets JSON pour éviter les erreurs de parsing. [#256](https://github.com/betagouv/OTP-DS-to-Grist/issues/256)

### Autres changements
- Mise à jour de la documentation pour afficher l'environnement d'exécution. [#254](https://github.com/betagouv/OTP-DS-to-Grist/issues/254)
- Suppression des détails unitaires des temps d'appels dans la progression de la synchronisation pour une meilleure lisibilité. [#273](https://github.com/betagouv/OTP-DS-to-Grist/issues/273)
- Correction de la création de la table "avis". [#265](https://github.com/betagouv/OTP-DS-to-Grist/issues/265)
