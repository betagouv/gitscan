## Changelog : meet (30 derniers jours, au 16 novembre 2026)

### Résumé
Ce mois-ci, Meet a franchi une étape majeure dans l'amélioration de son accessibilité et de sa sécurité. L'interface est désormais plus inclusive grâce à de nombreux ajustements pour les utilisateurs en situation de handicap, et le support de la langue portugaise a été ajouté. Parallèlement, une campagne importante de renforcement de la sécurité a été menée pour protéger les données et les échanges, tout en optimisant l'infrastructure technique.

### Évolutions fonctionnelles
- **Accessibilité (A11y) :**
    - Amélioration de la navigation au clavier (gestion de la touche Échap pour fermer les dialogues [#1916]).
    - Optimisation de la lecture par synthèse vocale : ajout de titres explicites, de noms pour les boutons de transcription et d'annonces pour les changements d'état (ex: micro coupé).
    - Amélioration de la visibilité : correction des contrastes de couleurs et ajout de l'indicateur de focus sur les cartes de test de connexion.
- **Internationalisation :** Ajout du support complet de la langue portugaise.
- **Expérience utilisateur (UX) :**
    - Amélioration du carrousel de participants pour mettre en avant les nouveaux intervenants et les mains levées.
    - Meilleure gestion des erreurs : affichage de messages explicites lors d'échecs de connexion ou d'interruptions d'enregistrement.
    - Remplacement du chat Crisp par le formulaire de support officiel de La Suite.
- **Confidentialité :** Protection des salles de réunion contre l'indexation par les moteurs de recherche et les outils d'IA.

### Évolutions techniques
- **Sécurité et conformité :**
    - Mise en place d'un système d'audit logging structuré pour tracer les actions sensibles (enregistrements, transcriptions, résumés).
    - Renforcement de la protection des données : sanitisation des logs, gestion sécurisée des secrets et protection des URLs signées.
    - Correction de nombreuses vulnérabilités (CVE) sur les composants critiques (Nginx, Node.js, Pillow, aiohttp, etc.).
- **Infrastructure et Performance :**
    - Optimisation des images Docker (utilisation de Nginx non-privilégié et support natif pour l'architecture arm64).
    - Mise à jour de l'infrastructure LiveKit (serveur et egress) et amélioration de la politique de reconnexion automatique.
    - Optimisation du chargement des illustrations via le format WebP.
- **Fiabilité Backend :** Amélioration de la gestion des timeouts et des erreurs lors des appels à l'API LiveKit.

### Autres changements
- **Documentation :** Création d'un nouveau site de documentation complet pour le projet.
- **Qualité de code :** Nettoyage des scripts d'installation et mise à jour des outils de vérification (shellcheck, gitlint).
