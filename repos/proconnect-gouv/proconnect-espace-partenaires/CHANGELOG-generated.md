## Changelog : proconnect-espace-partenaires (30 derniers jours, au 19 juin 2026)

### Résumé
Les dernières mises à jour se concentrent principalement sur l'amélioration de la documentation concernant l'eIDAS et l'ANSSI, ainsi que sur des corrections de documentation existantes. Des ajustements ont également été apportés pour clarifier les informations relatives aux niveaux d'eIDAS et aux données fournies par les fournisseurs de services. Enfin, quelques corrections mineures et mises à jour de dépendances ont été intégrées.

### Évolutions fonctionnelles
- Suppression d'une note de prudence concernant la définition du niveau ACR.
- Suppression des anciennes adresses IP utilisées dans le projet [#360](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/360).

### Évolutions techniques
- Mise à jour de la dépendance `proconnect-gouv/federation/api-partner` vers les versions `0a2e92c`, `67f9044` et `6f9044`.
- Mises à jour de dépendances de développement : `actions/checkout`, `esbuild`, `@uuv/playwright`, `tsx`, `@playwright/test`, `fast-xml-parser` et `@aws-sdk/xml-builder`.

### Autres changements
- Amélioration de la documentation eIDAS : ajout de la norme eIDAS à la barre latérale et intégration des distinctions du guide ANSSI [#367](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/367).
- Clarification de la distinction entre eIDAS1-MFA et eIDAS2 dans la documentation [#349](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/349).
- Restructuration de la documentation des données fournies pour clarifier leur origine [#317](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/317).
- Ajout de la documentation pour `organization_label` [#348](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/348) et ajout d'une mention dans la table des matières.
- Suppression d'une exigence d'autorisation obsolète pour les rôles [#353](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/353).
- Correction d'une faute de frappe [#354](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/354).
- Regroupement des données additionnelles et complémentaires dans la documentation [#347](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/347).
- Clarification des niveaux eIDAS pour les fournisseurs de services [#352](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/352).
- Mise à jour d'informations inexactes dans les tests d'identifiants FI [#346](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/346).
