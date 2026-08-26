## Changelog : egapro (30 derniers jours, au 25 août 2026)

### Résumé
Ce mois-ci, les développements ont principalement porté sur l'amélioration de l'expérience utilisateur, notamment via l'optimisation de l'espace personnel ("Mon espace") et la fiabilisation du parcours de déclaration des rémunérations. Des efforts significatifs ont également été consacrés au renforcement de l'accessibilité, à l'extension de la couverture des tests automatisés et à la sécurisation des échanges techniques.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités et interface utilisateur**
    - Mise en place de la "représentation équilibrée" ([#4203](https://github.com/SocialGouv/egapro/issues/4203)).
    - Refonte de la modale "Mon profil" pour une meilleure conformité visuelle et l'ajout des mentions d'obligation ([#4188](https://github.com/SocialGouv/egapro/issues/4188)).
    - Amélioration de l'ergonomie globale (alignements sur les maquettes Figma, typographies et gestion des couleurs) ([#4271](https://github.com/SocialGouv/egapro/issues/4271), [#4174](https://github.com/SocialGouv/egapro/issues/4174)).
- **Parcours de déclaration et rémunération**
    - Correction de la logique de calcul des indicateurs (ratios, décimales et synchronisation des données GIP) ([#4121](https://github.com/SocialGouv/egapro/issues/4121), [#4039](https://github.com/SocialGouv/egapro/issues/4039), [#4048](https://github.com/SocialGouv/egapro/issues/4048)).
    - Renforcement des règles de validation (blocage de l'accès au tunnel sans informations obligatoires comme le téléphone ou le CSE) ([#4117](https://github.com/SocialGouv/egapro/issues/4117)).
    - Amélioration de la clarté des libellés et des étapes de la démarche ([#4239](https://github.com/SocialGouv/egapro/issues/4239), [#4274](https://github.com/SocialGouv/egapro/issues/4274)).
- **Espace utilisateur ("Mon espace")**
    - Optimisation de l'affichage des démarches en cours et de la gestion des erreurs liées au CSE ([#4229](https://github.com/SocialGouv/egapro/issues/4229), [#4263](https://github.com/SocialGouv/egapro/issues/4263)).
    - Amélioration de la visibilité des récapitulatifs de déclaration dès leur soumission ([#4130](https://github.com/SocialGouv/egapro/issues/4130)).
- **Accessibilité et Documents**
    - Intégration de l'outil `ultra11y` pour renforcer l'accessibilité de la plateforme ([#4169](https://github.com/SocialGouv/egapro/issues/4169)).
    - Corrections sur la génération des documents PDF (gestion des titres orphelins et des en-têtes de tableaux) ([#4257](https://github.com/SocialGouv/egapro/issues/4257), [#4145](https://github.com/SocialGouv/egapro/issues/4145)).

### Évolutions techniques
- **Qualité et Tests**
    - Extension massive de la couverture des tests de bout en bout (E2E) sur l'ensemble des parcours ([#4097](https://github.com/SocialGouv/egapro/issues/4097)).
    - Amélioration de la fiabilité des environnements de développement et de l'authentification des nouveaux worktrees ([#4095](https://github.com/SocialGouv/egapro/issues/4095)).
- **Infrastructure et CI/CD**
    - Optimisation du pipeline de déploiement et de la gestion des versions des images de test ([#4057](https://github.com/SocialGouv/egapro/issues/4057)).
    - Automatisation et fiabilisation du processus de release via le CLI ([#4009](https://github.com/SocialGouv/egapro/issues/4009)).
- **Sécurité et API**
    - Mise en place du certificat client mTLS pour sécuriser les appels vers SUIT ([#4101](https://github.com/SocialGouv/egapro/issues/4101)).
    - Amélioration de la documentation de l'API publique concernant la convention des ratios d'écarts ([#4041](https://github.com/SocialGouv/egapro/issues/4041)).

### Autres changements
- Mise à jour de la documentation technique, notamment sur la nomenclature des cas de tests ([#4006](https://github.com/SocialGouv/egapro/issues/4006)).
- Maintenance des outils d'accessibilité.
