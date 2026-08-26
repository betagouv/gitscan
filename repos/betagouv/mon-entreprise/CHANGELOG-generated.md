## Changelog : mon-entreprise (30 derniers jours, au 24 août 2026)

### Résumé
Ce mois a été marqué par une modernisation profonde de l'architecture des simulateurs et de l'infrastructure de déploiement. Ces évolutions techniques permettent une gestion plus robuste des données et une accélération des cycles de test. Côté utilisateur, la précision des calculs (SMIC, retraites) a été renforcée et l'interface a bénéficié de plusieurs améliorations visuelles et correctifs de navigation.

### Évolutions fonctionnelles
- **Précision des calculs** : Correction de la valeur du SMIC utilisée pour le calcul de la RGDU et mise à jour des taux de la retraite complémentaire (CARMF et CARCDSF) pour 2026.
- **Interface utilisateur** : 
    - Ajout de nouvelles images de prévisualisation pour les simulateurs et pour la page "demande de mobilité".
    - Corrections de coquilles dans le message de contact du footer.
    - Ajustements ergonomiques (centrage de boutons, styles de texte).
- **Navigation** : Correction de la gestion des erreurs pour afficher correctement la page 404.

### Évolutions techniques
- **Refonte du système de simulation** : Restructuration majeure pour séparer les métadonnées (SEO, plan du site) des configurations de routage. Cette simplification facilite la maintenance et l'ajout de nouveaux simulateurs.
- **Automatisation du déploiement (CI/CD)** : 
    - Mise en place de "review apps" sur Clever Cloud : chaque Pull Request génère désormais un environnement de test temporaire avec un lien direct pour validation.
    - Optimisation des processus de déploiement et de la gestion des ressources sur Clever Cloud.
- **Optimisation de l'API** : Refactorisation des middlewares, de la gestion du cache et amélioration de l'accessibilité des modèles TI et AS via l'API.
- **Performance et maintenance** : 
    - Chargement à la demande de certains composants lourds pour améliorer la vitesse d'affichage.
    - Mise à jour des outils de développement (TypeScript, Vite, Vitest, Prettier).
    - Nettoyage important du code mort et des types obsolètes.

### Autres changements
- **Documentation** : Mise à jour des guides sur l'infrastructure Clever Cloud, les métadonnées des simulateurs et les précisions sur les calculs de SMIC.
- **Gestion des assets** : Nettoyage et réorganisation des fichiers images et illustrations.
