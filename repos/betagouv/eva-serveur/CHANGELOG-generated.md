## Changelog : eva-serveur (30 derniers jours, au 24 septembre 2026)

### Résumé
Ce mois a été marqué par une modernisation importante de l'interface utilisateur pour s'aligner sur les standards DSFR et une refonte majeure du système de génération de documents PDF pour plus de fiabilité. Les capacités de gestion des données ont été enrichies (données sociodémographiques et santé) et l'infrastructure a été mise à jour vers les dernières versions de Rails et Ruby pour garantir la stabilité et la performance du serveur.

### Évolutions fonctionnelles
- **Modernisation de l'interface (UI/UX) :**
    - Adoption des composants DSFR pour les cartes d'actualités, les badges et les boutons.
    - Mise en place d'un design responsive (grille DSFR) et amélioration de l'affichage sur mobile.
    - Amélioration de l'accessibilité : gestion des erreurs de connexion sous les champs de saisie, indication des types de champs pour les lecteurs d'écran et éclaircissement des contrastes.
    - Amélioration de la navigation : les cartes d'actualités sont désormais entièrement cliquables.
- **Gestion des données et structures :**
    - Amélioration de la validation des SIRET : distinction entre un SIRET invalide et un SIRET fermé, et ajout d'alertes pour les administrateurs en cas de SIRET non vérifiable.
    - Inclusion des données sociodémographiques et de santé dans les exports d'évaluations EVA.
    - Possibilité pour les conseillers de modifier les informations des bénéficiaires.
- **Expérience de génération PDF :**
    - Nouvelle interface de téléchargement avec une modale de suivi permettant de patienter pendant la génération.
    - Possibilité de lancer plusieurs générations de PDF simultanément.
- **Pilotage des restitutions :**
    - Ajout d'un bouton pour forcer le recalcul d'une restitution et affichage du nombre d'événements concernés.

### Évolutions techniques
- **Mises à jour majeures :**
    - Migration du framework vers Rails 8.0.5.
    - Mise à jour de la version de Ruby (4.0.6).
- **Optimisation du moteur PDF :**
    - Déportation de la génération de PDF dans des tâches de fond (Sidekiq) avec notification en temps réel (ActionCable).
    - Amélioration de la gestion de la mémoire et de la stabilité de Chromium (redémarrage nocturne, gestion des crashs et verrouillage des accès concurrents).
    - Accélération du service des fichiers PDF en les servant directement depuis le disque.
- **Performance et robustesse :**
    - Optimisation du calcul de la complétude des évaluations et du redimensionnement des images.
    - Renforcement de la sécurité contre les attaques par rafale de requêtes via l'implémentation de `Rack::Attack`.
    - Amélioration de la résilience de l'API en cas d'indisponibilité des services tiers (SIRENE).

### Autres changements
- **Maintenance et tests :**
    - Enrichissement des jeux de données de test (données d'opérateurs de compétences, illustrations, parcours types).
    - Nettoyage de code et harmonisation des traductions en français.
    - Correction de divers bugs mineurs (favicons, icônes iOS, erreurs de routage).
