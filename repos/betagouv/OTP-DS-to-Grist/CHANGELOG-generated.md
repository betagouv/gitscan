## Changelog : OTP-DS-to-Grist (30 derniers jours, au 17 octobre 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape importante avec l'intégration de nouveaux agents d'intelligence artificielle et un renforcement significatif de la sécurité. Les performances de synchronisation ont également été optimisées pour offrir une expérience plus fluide et une gestion des données plus fiable.

### Évolutions fonctionnelles
- **Intelligence Artificielle :** Expansion des capacités avec l'ajout de nouveaux agents (dn, grist, @logs) et mise à jour de l'agent reviewer.
- **Expérience utilisateur :**
    - Mise en place de l'auto-enregistrement multiple ([#514](https://github.com/betagouv/OTP-DS-to-Grist/issues/514)).
    - Amélioration de l'interface de synchronisation via la correction du bandeau d'affichage ([#512](https://github.com/betagouv/OTP-DS-to-Grist/issues/512)) et la synchronisation forcée lors du changement de filtre ([#488](https://github.com/betagouv/OTP-DS-to-Grist/issues/488)).
- **Corrections :** Résolution de la perte de données dans les champs "carte" ([#497](https://github.com/betagouv/OTP-DS-to-Grist/issues/497)) et correction de l'OCR dans les colonnes de pièces jointes ([#558](https://github.com/betagouv/OTP-DS-to-Grist/issues/558)).

### Évolutions techniques
- **Sécurité et Authentification :**
    - Implémentation de l'authentification via les tokens Grist ([#566](https://github.com/betagouv/OTP-DS-to-Grist/issues/566), [#562](https://github.com/betagouv/OTP-DS-to-Grist/issues/562)).
    - Renforcement de la protection du service avec l'ajout de Fail2ban ([#547](https://github.com/betagouv/OTP-DS-to-Grist/issues/547)), la restriction des URLs Grist ([#551](https://github.com/betagouv/OTP-DS-to-Grist/issues/551)) et une meilleure logique de vérification des accès ([#574](https://github.com/betagouv/OTP-DS-to-Grist/issues/574)).
- **Optimisation de la synchronisation :**
    - Amélioration des performances via la récupération des dossiers par lots ([#536](https://github.com/betagouv/OTP-DS-to-Grist/issues/536)) et l'optimisation des mécanismes de cache pour Grist ([#554](https://github.com/betagouv/OTP-DS-to-Grist/issues/554)) et les blocs répétables ([#504](https://github.com/betagouv/OTP-DS-to-Grist/issues/504)).
    - Fiabilisation de la gestion des lignes répétables ([#549](https://github.com/betagouv/OTP-DS-to-Grist/issues/549)) et isolation de la gestion des limites de débit (rate-limiting) ([#534](https://github.com/betagouv/OTP-DS-to-Grist/issues/534)).
- **Corrections techniques :** Résolution des échecs de lecture Grist ([#555](https://github.com/betagouv/OTP-DS-to-Grist/issues/555)).

### Autres changements
- Organisation et maintenance du module DN ([#515](https://github.com/betagouv/OTP-DS-to-Grist/issues/515)).
- Correction des chemins pour les ressources statiques (polices de caractères).
