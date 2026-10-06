## Changelog : mycollections (30 derniers jours, au 05/10/2026)

### Résumé
Cette période a été marquée par une maturation importante de l'interface utilisateur et un renforcement de la fiabilité du système. L'expérience est devenue plus intuitive grâce à une meilleure navigation (catalogue repliable, fil d'Ariane), un ton plus professionnel (vouvoiement) et une gestion améliorée des retours utilisateurs (système de demandes). Côté technique, le projet a gagné en robustesse avec une meilleure gestion de l'indexation des documents et une intégration plus poussée avec les services de l'écosystème (Bus de la bêta).

### Évolutions fonctionnelles
- **Recherche et Catalogue** : 
    - Mise en place d'une nouvelle API de recherche conforme aux contrats MirAI [#58](https://github.com/IA-Generative/mycollections/pull/58).
    - Introduction de catégories repliables dans le catalogue pour une meilleure lisibilité [#42](https://github.com/IA-Generative/mycollections/pull/42).
    - Ajout d'animations de chargement pour le catalogue et d'indicateurs de résultats de recherche.
- **Expérience Utilisateur (UX/UI)** :
    - Harmonisation du ton (utilisation du vouvoiement) et amélioration de l'accessibilité (gestion du focus, menus mobiles).
    - Ajout d'un fil d'Ariane et de messages d'erreur clairs en français.
    - Amélioration de la visibilité des sources dans l'assistant (titres, sections et extraits lisibles).
- **Gestion des Collections et Fiches** :
    - Nouvelle fonctionnalité « Où interroger cette collection » pour orienter l'utilisateur vers les bons outils [#23](https://github.com/IA-Generative/mycollections/pull/23).
    - Amélioration de la gestion des partages et de la visibilité des états de publication.
- **Interaction et Feedback** :
    - Déploiement d'un système complet de « Demandes » et de satisfaction pour permettre aux usagers d'être acteurs du projet [#39](https://github.com/IA-Generative/mycollections/pull/39).
    - Accessibilité accrue de la section « Mon avis » en plein écran.
- **Visualisation (Graphe)** :
    - Passage en mode plein écran pour le graphe et possibilité d'importer des graphes construits hors du système [#36](https://github.com/IA-Generative/mycollections/pull/36).

### Évolutions techniques
- **Sécurité et Accès** :
    - Renforcement de l'authentification via Keycloak (gestion des scopes et des jetons) et contrôle des accès basé sur des groupes spécifiques.
    - Sécurisation des routes et des liens partagés via un proxy pour éviter les erreurs d'accès aux fichiers.
- **Indexation et Données** :
    - Amélioration de la résilience de l'indexation : le processus peut désormais reprendre là où il s'est arrêté après un redémarrage.
    - Optimisation de la réindexation pour éviter la duplication des données (corpus et sources).
    - Amélioration du découpage des documents (chunking) pour une meilleure précision.
- **Infrastructure et CI/CD** :
    - Migration de la gestion des dépendances vers `uv` pour plus de rapidité et de fiabilité.
    - Mise en place d'une suite de tests de bout en bout (E2E) couvrant les parcours critiques (création, publication, accès) [#47](https://github.com/IA-Generative/mycollections/pull/47).
    - Ajout d'un endpoint de santé (`/health`) pour surveiller l'état du service et de ses dépendances [#46](https://github.com/IA-Generative/mycollections/pull/46).
- **Intégration Système** :
    - Connexion au « Bus » de la bêta pour automatiser le suivi des demandes et des signalements [#11](https://github.com/IA-Generative/mycollections/pull/11).

### Autres changements
- **Documentation** : Mise à jour des guides de déploiement (procédure neutre) et enrichissement du README.
- **Nettoyage** : Alignement de la nomenclature sur les standards de la bêta et retrait des identifiants d'infrastructure du code source.
