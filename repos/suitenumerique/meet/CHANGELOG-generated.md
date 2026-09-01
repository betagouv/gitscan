## Changelog : meet (30 derniers jours, au 31 août 2026)

### Résumé
Ce mois-ci, meet a franchi une étape importante dans l'amélioration de l'expérience utilisateur et de la gestion des réunions. Les utilisateurs bénéficient désormais de nouveaux outils de test (connexion et son), d'un support pour l'espagnol et d'une interface mieux adaptée aux mobiles. Les fonctionnalités de gestion ont été renforcées, permettant aux utilisateurs authentifiés de mieux contrôler les salles de confiance. Parallèlement, une attention majeure a été portée à la robustesse technique, notamment via la sécurisation des processus de déploiement et la résolution de problèmes critiques liés à l'accès aux périphériques média.

### Évolutions fonctionnelles
- **Gestion et administration** :
    - Possibilité pour les utilisateurs authentifiés de gérer le lobby dans les salles de confiance et de promouvoir des participants.
    - Ajout d'une fenêtre de configuration de salle lors de la création de réunions.
    - Introduction de badges pour identifier les participants non authentifiés.
- **Expérience utilisateur et accessibilité** :
    - Ajout du support de la langue espagnole et amélioration de la clarté des textes de l'interface.
    - Nouveaux outils de diagnostic : tests de connexion et tests de sortie audio (haut-parleurs).
    - Amélioration de l'accessibilité : fermeture des panneaux latéraux avec la touche `Échap` et meilleures notifications lors des changements de rôle.
    - Optimisation de l'affichage mobile : meilleure réactivité des écrans de feedback et réorganisation des contrôles sur petits écrans.
- **Interface** :
    - Notifications visuelles lors du changement de rôle d'un participant.
    - Amélioration de l'affichage des avatars (initiales en majuscules et gestion des caractères Unicode).

### Évolutions techniques
- **Infrastructure et CI/CD** :
    - Renforcement de la sécurité et de la fiabilité du pipeline CI (utilisation de `uv` pour Python, verrouillage des versions des actions et sécurisation des téléchargements).
- **Performance et stabilité** :
    - Optimisation des performances backend via le remplacement des commandes Redis bloquantes par des scans basés sur curseurs.
    - Correction massive de bugs liés à l'accès aux périphériques (caméra/micro) sur Chrome, Firefox et Windows, et gestion plus fluide des erreurs de partage d'écran.
    - Optimisation de la gestion des pistes audio et réduction des re-rendus inutiles de l'interface.
- **Architecture** :
    - Refactorisation de composants clés du frontend (gestion des participants, processus d'entrée en réunion et panneaux latéraux).
    - Restructuration de services backend (gestion SIP, client S3 et gestion des jetons utilisateurs).
    - Amélioration de la télémétrie et du suivi des erreurs pour un meilleur diagnostic technique.

### Autres changements
- Mise à jour de la documentation technique et des conditions générales d'utilisation.
- Ajout du fichier `publiccode.yml` pour la conformité.
