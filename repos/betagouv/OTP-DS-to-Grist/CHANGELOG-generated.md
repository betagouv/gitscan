## Changelog : OTP-DS-to-Grist (30 derniers jours, au 08/10/2026)

### Résumé
Ce mois-ci, le connecteur a considérablement gagné en robustesse et en rapidité. Les utilisateurs peuvent désormais gérer la synchronisation automatique de plusieurs démarches simultanément. Des améliorations majeures ont été apportées à la sécurité du système et à la performance du traitement des données, tout en corrigeant des problèmes d'affichage et de perte de données sur certains champs.

### Évolutions fonctionnelles
- **Multi-démarches :** Gestion de la synchronisation automatique pour plusieurs démarches simultanément ([#491](https://github.com/betagouv/OTP-DS-to-Grist/issues/491)).
- **Expérience utilisateur :**
    - La synchronisation est désormais forcée automatiquement lors du changement de filtre ([#488](https://github.com/betagouv/OTP-DS-to-Grist/issues/488)).
    - Correction de l'affichage du bandeau de suivi de synchronisation ([#512](https://github.com/betagouv/OTP-DS-to-Grist/issues/512)).
- **Fiabilité des données :** Correction d'un problème entraînant la perte de données dans les champs de type "carte" ([#497](https://github.com/betagouv/OTP-DS-to-Grist/issues/497)).
- **Intelligence Artificielle :** Mise à jour des capacités des agents IA.

### Évolutions techniques
- **Performance & Optimisation :**
    - Accélération de la synchronisation via la récupération des dossiers par lots ([#536](https://github.com/betagouv/OTP-DS-to-Grist/issues/536)).
    - Optimisation du cache pour les blocs répétables afin de réduire le temps d'exécution ([#504](https://github.com/betagouv/OTP-DS-to-Grist/issues/504)).
- **Sécurité :**
    - Mise en place de protections contre les attaques par force brute via Fail2Ban ([#547](https://github.com/betagouv/OTP-DS-to-Grist/issues/547)).
    - Restriction des URLs Grist autorisées pour sécuriser les échanges ([#551](https://github.com/betagouv/OTP-DS-to-Grist/issues/551)).
- **Robustesse du système :**
    - Amélioration de l'auto-sauvegarde pour les contextes multi-démarches ([#514](https://github.com/betagouv/OTP-DS-to-Grist/issues/514)).
    - Correction de la gestion des clés pour les lignes répétables ([#549](https://github.com/betagouv/OTP-DS-to-Grist/issues/549)).
    - Refactorisation de la gestion des sessions avec limitation de débit (rate limiting) pour une meilleure stabilité ([#534](https://github.com/betagouv/OTP-DS-to-Grist/issues/534)).

### Autres changements
- **Documentation :** Mises à jour régulières du README et de la documentation des agents.
- **Infrastructure & Dev :**
    - Nettoyage de la configuration Docker et amélioration du support pour les environnements Codespaces ([#509](https://github.com/betagouv/OTP-DS-to-Grist/issues/509)).
    - Maintenance de modules internes ([#515](https://github.com/betagouv/OTP-DS-to-Grist/issues/515)).
- **Interface :** Correction des chemins de polices de caractères pour le design système DSFR.
