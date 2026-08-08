## Changelog : mon-entreprise (30 derniers jours, au 07 août 2026)

### Résumé
Ce mois a été marqué par une refonte majeure de l'architecture technique des simulateurs pour améliorer la maintenance du projet, ainsi que par le lancement du nouveau simulateur pour les travailleurs frontaliers en Suisse. Parallèlement, l'infrastructure a évolué avec le déploiement des applications Next.js sur Clever Cloud et une amélioration significative de l'internationalisation (i18n) de la plateforme.

### Évolutions fonctionnelles
- **Nouveau simulateur** : Mise en ligne du simulateur de cotisation maladie pour les travailleurs frontaliers en Suisse, incluant une nouvelle expérience utilisateur et la possibilité de partager une simulation via l'URL.
- **Améliorations de l'interface** :
    - Optimisation de l'affichage du comparateur de statuts.
    - Mise à jour des visuels et des images de prévisualisation pour les simulateurs.
    - Amélioration de la gestion des erreurs (comportement de la page 404).
- **Corrections de calculs et règles métier** :
    - Correction du calcul de la RGDU (ajustement de la valeur du Smic utilisée).
    - Correction de l'application de la réforme de l'Acre (basée sur la date de création de l'entreprise).
    - Ajustement des taux de retraite complémentaire (CARMF et CARCDSF).
    - Correction des arrondis pour les conjoints collaborateurs (Cipav).
    - Correction de la participation de la CPAM dans le cadre du PAMC.

### Évolutions techniques
- **Refonte de l'architecture des simulateurs** : Restructuration profonde pour séparer les métadonnées (données pures) de la configuration des pages (composants, SEO, routage). Ce changement simplifie l'ajout de nouveaux simulateurs et optimise le plan du site.
- **Infrastructure et CI/CD** :
    - Automatisation du déploiement des applications Next.js sur Clever Cloud.
    - Amélioration des tests automatisés pour supporter le déploiement multi-langues.
- **Internationalisation (i18n)** : Refonte du système de traduction pour assurer la cohérence des dates, de la documentation (MDX) et des métadonnées selon la langue sélectionnée.
- **Optimisation de l'API** : Refactorisation des middlewares, de la gestion du cache et amélioration de l'accessibilité des modèles TI et AS.
- **Design System** :
    - Amélioration de la robustesse des composants (Switch, Iframe, Navigation).
    - Normalisation de la gestion des assets (images/icônes) entre les environnements Vite et Next.js.

### Autres changements
- **Documentation** : Mise à jour des guides d'infrastructure (Clever Cloud) et de la documentation technique de la librairie de calcul.
- **Nettoyage** : Suppression des composants, des images et des commentaires de code obsolètes pour alléger le dépôt.
