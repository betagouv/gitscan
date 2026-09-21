## Changelog : proconnect-identite (30 derniers jours, au 18 septembre 2026)

### Résumé
Ce mois-ci, ProConnect Identité a renforcé la sécurité et la protection de la vie privée, notamment par l'anonymisation des données exportées et la correction de failles de contournement. Les informations sur les organisations ont été fiabilisées grâce à l'intégration de l'API RNE, et l'expérience utilisateur a été améliorée avec la possibilité de déconnecter un compte FranceConnect.

### Évolutions fonctionnelles
- **Sécurité** : Correction d'une faille permettant de contourner le code de contact officiel.
- **Sécurité** : Amélioration des alertes de sécurité par email, incluant désormais le nom de la clé d'accès supprimée [#2163](https://github.com/proconnect-gouv/proconnect-identite/issues/2163).
- **Confidentialité** : Anonymisation des fonctions occupées (jobs) et suppression de ces données dans les exports [#2167](https://github.com/proconnect-gouv/proconnect-identite/issues/2167).
- **Données d'organisation** : Amélioration de la précision des informations d'établissement via l'intégration de l'API RNE et ajout de la dénomination usuelle [#2082](https://github.com/proconnect-gouv/proconnect-identite/issues/2082).
- **Expérience utilisateur** : Possibilité de déconnecter une identité FranceConnect [#2062](https://github.com/proconnect-gouv/proconnect-identite/issues/2062) et gestion des liens en attente [#2126](https://github.com/proconnect-gouv/proconnect-identite/issues/2126).
- **Corrections** : Résolution de fautes de frappe dans l'interface et les emails de MFA.

### Évolutions techniques
- **Architecture** : Création d'un dépôt dédié pour la gestion des informations utilisateur FranceConnect [#2159](https://github.com/proconnect-gouv/proconnect-identite/issues/2159).
- **Refactoring** : Homogénéisation de l'utilisation des méthodes de dépôt (`get` vs `find`) et du processus de vérification des contacts officiels [#2131](https://github.com/proconnect-gouv/proconnect-identite/issues/2131).
- **Sécurité & SEO** : Blocage de l'indexation par les moteurs de recherche via `robots.txt` [#8c8e037](https://github.com/proconnect-gouv/proconnect-identite/issues/8c8e037) et amélioration de la gestion des limites de débit (rate limiting) [#2138](https://github.com/proconnect-gouv/proconnect-identite/issues/2138).
- **Autonomie** : Localisation de certaines données et types (TrancheEffectifs, types d'authentificateurs) pour réduire la dépendance aux API externes [#2155](https://github.com/proconnect-gouv/proconnect-identite/issues/2155), [#2156](https://github.com/proconnect-gouv/proconnect-identite/issues/2156).
- **CI/CD & Tests** : Optimisation du workflow de release [#2146](https://github.com/proconnect-gouv/proconnect-identite/issues/2146), ajout d'une commande de test en mode "watch" [#2137](https://github.com/proconnect-gouv/proconnect-identite/issues/2137) et amélioration de la couverture de tests sur la liste des établissements [#2133](https://github.com/proconnect-gouv/proconnect-identite/issues/2133).
- **Automatisation** : Amélioration de la synchronisation quotidienne des listes d'administrations via Grist.

### Autres changements
- **Nettoyage** : Suppression de code de test inutile [#2169](https://github.com/proconnect-gouv/proconnect-identite/issues/2169).
- **Correction** : Normalisation des noms (suppression des diacritiques) pour les processus de certification [#2176](https://github.com/proconnect-gouv/proconnect-identite/issues/2176).
