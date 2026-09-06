## Changelog : meet (30 derniers jours, au 05/09/2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de la qualité vidéo avec l'introduction du 1080p, l'expansion linguistique avec l'ajout de l'espagnol et une optimisation de l'expérience sur mobile. Le projet a également bénéficié d'un renforcement significatif de sa sécurité et de ses outils de développement pour garantir une plateforme plus stable et performante.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités**
    - Ajout d'une option de résolution d'envoi en 1080p [#1660](https://github.com/suitenumerique/meet/issues/1660).
    - Support de l'espagnol pour l'interface utilisateur.
    - Intégration du moteur d'inférence Voxtral en temps réel pour les agents.
    - Possibilité pour les utilisateurs authentifiés de gérer le lobby dans les salles de confiance.
    - Nouveaux outils audio : indicateur de niveau (gauge) pour le micro et testeur de son pour la sortie.
- **Améliorations et Accessibilité**
    - Optimisation de l'interface mobile (réactivité des écrans de retour et de la barre de contrôle).
    - Améliorations de l'accessibilité : fermeture des panneaux latéraux avec la touche `Échap` [#1507](https://github.com/suitenumerique/meet/issues/1507) et guides pour la gestion des permissions de médias par le navigateur.
    - Améliorations visuelles : intensité du flou d'arrière-plan accrue et centrage des initiales des avatars.
- **Corrections**
    - Résolution de bugs liés au partage d'écran et à la gestion des périphériques (erreurs de type "device-in-use").
    - Correction du champ de saisie du chat et de l'affichage des notifications de connexion.

### Évolutions techniques
- **Backend & Performance**
    - Ajout du support du proxy inverse Traefik pour l'authentification des médias [#1649](https://github.com/suitenumerique/meet/issues/1649).
    - Optimisation des performances Redis via l'utilisation de `SCAN` au lieu de `KEYS`.
    - Mise à jour dynamique des attributs de salle via l'API externe.
- **Infrastructure & CI/CD**
    - Durcissement de la pipeline CI/CD (utilisation de `uv`, verrouillage des versions des actions GitHub et sécurisation des téléchargages).
    - Mise à jour du serveur LiveKit vers la version 1.13.6.
    - Amélioration de l'expérience de développement avec l'ajout d'un serveur TURN local et d'outils de diagnostic WebRTC/réseau.
- **Sécurité**
    - Correction de vulnérabilités critiques (CVE) dans la bibliothèque `libexpat`.

### Autres changements
- **Documentation & Internationalisation**
    - Mise à jour de la documentation de montée de version (`UPGRADE.md`).
    - Amélioration des traductions backend et de la clarté du langage de l'interface.
