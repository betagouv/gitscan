## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 13 août 2026)

### Résumé
Ce mois-ci, la plateforme a franchi une étape majeure dans l'expérience utilisateur avec l'introduction d'une personnalisation poussée de l'affichage des dossiers. Les administrateurs bénéficient également d'un nouvel outil de rédaction d'emails plus moderne et intuitif. En coulisses, d'importants travaux de fond ont été menés pour accélérer la recherche, optimiser les performances de l'API et fiabiliser l'ensemble de la suite de tests automatisés.

### Évolutions fonctionnelles
- **Personnalisation de l'affichage (Usagers)** : Les utilisateurs peuvent désormais personnaliser les colonnes affichées dans leur liste de dossiers, avec un regroupement par section et l'affichage des valeurs choisies directement sur les cartes de dossiers.
- **Système de notifications** : Introduction de badges et de bandeaux "Nouveau message" (style DSFR) pour signaler visuellement les nouvelles interactions sur les dossiers.
- **Nouvel éditeur d'emails (Administration)** : Migration des modèles de mails vers un éditeur riche (Tiptap) offrant une prévisualisation en direct, une gestion améliorée des tags et une interface plus ergonomique.
- **Amélioration de la collecte d'avis** : Optimisation du module "Je donne mon avis" (MonAvis) pour faciliter le retour d'expérience des usagers.
- **Accessibilité (A11y)** : Amélioration de l'annonce des notifications et des messages d'erreur par les lecteurs d'écran pour une meilleure inclusion.
- **Données externes** : Intégration de nouveaux points de données via FranceConnect (notamment pour les étudiants boursiers, l'AAH et l'AEEH) et nouveaux endpoints pour l'ARS.

### Évolutions techniques
- **Optimisation des performances** : 
    - Accélération de la recherche plein texte via l'utilisation de vecteurs de recherche (`tsvectors`) stockés en base de données.
    - Optimisation des requêtes GraphQL par le regroupement de requêtes (batching) et le préchargement de données (preloading).
    - Amélioration de l'indexation de la base de données pour le tri des dossiers.
- **Modernisation de l'interface** : Remplacement de certaines bibliothèques tierces (Reach, Lucide, Heroicons) par des composants React-Aria et les icônes officielles du Design System (DSFR).
- **Fiabilisation des tests** : 
    - Migration de l'infrastructure de tests système de Selenium/Chrome vers Playwright.
    - Adoption massive de "seeds" (via la gem Oaken) pour rendre les tests plus rapides, stables et moins dépendants de l'état de la base de données.
- **Robustesse du traitement des fichiers** : Renforcement de la sécurité et de la gestion des erreurs lors de l'upload et du décodage des images (libvips).

### Autres changements
- **Internationalisation (i18n)** : Travail important de nettoyage pour extraire les textes en dur vers les fichiers de traduction.
- **Documentation** : Mise à jour des captures d'écran de la FAQ pour refléter les nouveaux changements d'interface.
- **Maintenance** : Nettoyage de code (migration de composants HAML vers ERB) et mise à jour des outils de linting.
