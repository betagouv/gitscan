## Changelog : meet (30 derniers jours, au 01/11/2026)

### Résumé
Ce mois a été marqué par un renforcement majeur de la sécurité et de la traçabilité du système, notamment via l'introduction d'un système d'audit complet. Les utilisateurs bénéficient également d'améliorations de l'accessibilité et de nouvelles options pour la gestion des enregistrements de réunions.

### Évolutions fonctionnelles
- **Enregistrements** : 
    - Possibilité pour les utilisateurs de choisir l'encodage de l'enregistrement.
    - Autorisation donnée à tout utilisateur authentifié de lancer un enregistrement.
- **Expérience utilisateur & Interface** :
    - Remplacement du chat Crisp par le formulaire de support officiel de La Suite.
    - Amélioration de la gestion de l'affichage : maintien du panneau d'administration lors du changement de paramètres et respect de l'état "main levée" en mode image dans l'image (PiP).
    - Test automatique du haut-parleur lorsqu'aucun périphérique de sortie n'est sélectionné.
    - Protection de la confidentialité : les salles de réunion sont désormais exclues des index des moteurs de recherche.
- **Accessibilité** :
    - Annonce vocale lors de la coupure du micro via un raccourci.
    - Amélioration de la navigation au clavier et de la lisibilité pour la pagination des participants.
    - Ajout de contours de focus visibles sur les éléments de menu.

### Évolutions techniques
- **Sécurité & Audit** :
    - Mise en place d'un système d'audit structuré permettant de tracer les actions sensibles (appels API, création d'utilisateurs, opérations sur les salles, enregistrements et transcriptions).
    - Renforcement de l'authentification : introduction d'un endpoint d'échange de tokens pour les intégrations en iframe et signature des identifiants de participants.
    - Sécurisation des secrets applicatifs via le hashage SHA-256 et restriction de l'édition des identifiants clients dans l'administration.
    - Application de nombreux correctifs de sécurité (CVE) sur des composants critiques (Nginx, Node.js, Django, Brotli, Pillow, aiohttp, etc.).
- **Backend & Performance** :
    - Optimisation des performances via l'ajout d'un pool de connexions `psycopg` et d'un index pour la recherche d'utilisateurs par email (insensible à la casse).
    - Amélioration de la robustesse : ajout de timeouts sur tous les appels à l'API LiveKit et gestion des erreurs de service en cas de dépassement de délai.
    - Gestion du cycle de vie des salles : implémentation de la suppression logique (soft delete) avec purge automatique après une période de rétention.
- **Infrastructure & CI/CD** :
    - Support natif des images Docker pour l'architecture arm64.
    - Mise à jour de l'infrastructure de résumé (FFmpeg 8.1.3).
    - Intégration de Vitest pour renforcer la couverture des tests unitaires côté frontend.
    - Mise à jour des charts Helm pour le déploiement.

### Autres changements
- **Documentation** : Mise à jour de la documentation de l'audit, du README et des guides de mise à niveau (UPGRADE.md).
- **Développement** : Nettoyage du code (suppression des `console.log`) et intégration de `gitlint` pour la validation des messages de commit.
