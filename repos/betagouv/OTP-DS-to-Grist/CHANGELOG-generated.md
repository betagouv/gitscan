## Changelog : OTP-DS-to-Grist (30 derniers jours, au 8 octobre 2026)

### Résumé
Cette période a été marquée par une amélioration significative de la gestion de la synchronisation, notamment avec l'introduction du support multi-démarches et l'optimisation des performances de traitement. La sécurité du service a également été renforcée par l'ajout de mécanismes de protection contre les abus et une meilleure restriction des accès.

### Évolutions fonctionnelles
- **Synchronisation multi-démarches :** Amélioration de la gestion de la synchronisation automatique pour permettre le traitement de plusieurs démarches simultanément ([#491](https://github.com/betagouv/OTP-DS-to-Grist/issues/491), [#514](https://github.com/betagouv/OTP-DS-to-Grist/issues/514)).
- **Expérience utilisateur :** 
    - Correction de l'affichage du bandeau de synchronisation pour garantir la cohérence des informations ([#512](https://github.com/betagouv/OTP-DS-to-Grist/issues/512)).
    - Déclenchement automatique de la synchronisation lors du changement de filtre pour une interface plus réactive ([#488](https://github.com/betagouv/OTP-DS-to-Grist/issues/488)).
- **Intégrité des données :** Résolution d'un problème causant la perte de données dans les champs de type "carte" ([#497](https://github.com/betagouv/OTP-DS-to-Grist/issues/497)).

### Évolutions techniques
- **Optimisation des performances :** 
    - Mise en place de la récupération des dossiers par lots pour accélérer les processus ([#536](https://github.com/betagouv/OTP-DS-to-Grist/issues/536)).
    - Optimisation du cache pour les blocs répétables afin de réduire la charge par cycle de synchronisation ([#504](https://github.com/betagouv/OTP-DS-to-Grist/issues/504)).
- **Sécurité :** 
    - Implémentation de Fail2Ban pour protéger l'application contre les tentatives d'accès malveillantes ([#547](https://github.com/betagouv/OTP-DS-to-Grist/issues/547)).
    - Restriction des URLs Grist autorisées ([#551](https://github.com/betagouv/OTP-DS-to-Grist/issues/551)).
- **Robustesse du moteur de synchronisation :** 
    - Amélioration de la gestion des clés pour les lignes répétables ([#549](https://github.com/betagouv/OTP-DS-to-Grist/issues/549)).
    - Refactorisation et isolation de la gestion du débit (rate-limiting) pour une meilleure stabilité ([#534](https://github.com/betagouv/OTP-DS-to-Grist/issues/534)).

### Autres changements
- **Documentation et Agents :** Mise à jour de la documentation (README) et des agents OpenCode ([#501](https://github.com/betagouv/OTP-DS-to-Grist/issues/501), [#515](https://github.com/betagouv/OTP-DS-to-Grist/issues/515)).
- **Infrastructure de développement :** Nettoyage de la configuration Docker et corrections pour l'environnement Codespaces ([#509](https://github.com/betagouv/OTP-DS-to-Grist/issues/509)).
- **Interface :** Correction des chemins de polices de caractères DSFR.
