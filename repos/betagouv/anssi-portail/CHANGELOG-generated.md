## Changelog : anssi-portail (30 derniers jours, au 11 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans les parcours de sécurisation et la gestion des mesures de sécurité. Des corrections de sécurité et des mises à jour techniques ont également été apportées pour garantir la stabilité et la robustesse de la plateforme. L'intégration du Design System Français (DSFR) continue, améliorant la cohérence visuelle et l'accessibilité.

### Évolutions fonctionnelles
- **Parcours de sécurisation :**
    - Ajout d'une indication visuelle pour les mesures de sécurité prises en compte.
    - Optimisation de la liste des mesures pour une meilleure performance.
    - Protection de la page et de l'API du module cyberdépart.
    - Affichage du badge de prise en compte sur les parcours de sécurisation.
    - Possibilité de prendre en compte les mesures de sécurité directement depuis l'interface.
    - Affichage de la progression dans le parcours de sécurisation.
- **Mesures de sécurité :**
    - Ajout d'un fil d'Ariane pour faciliter la navigation.
    - Affichage du titre de la mesure.
    - Limitation de la possibilité de donner un avis sur les mesures en mode connecté.
    - Affichage des actions prioritaires et des liens pour aller plus loin.
    - Affichage des risques associés à chaque mesure.
    - Affichage des exigences ReCyF liées aux mesures.
    - Ajout d'un encart "tutoriel" pour les mesures.
    - Possibilité de soumettre des retours sur les mesures.
- **Collectivités :** Ajout d'une ancre pour afficher la demande de diagnostic.
- **Interface utilisateur :**
    - Amélioration de la page 404.
    - Utilisation du composant DSFR pour les badges, les boutons, les sélecteurs, le fil d'Ariane et la navigation tertiaire.
    - Correction de l'affichage des erreurs de la demande de diagnostic.
    - Simplification des styles des titres.
    - Amélioration de l'accessibilité des sélecteurs avec ajout d'IDs.
    - Ajustement des marges et de l'affichage général de certains composants.
- **Contacts :** Mise à jour des informations des contacts régionaux (PACA, ARA, Normandie).

### Évolutions techniques
- **Sécurité :**
    - Correction d'une vulnérabilité.
    - Validation du token.
    - Vérification du niveau de sécurité de l'utilisateur et récupération des informations MFA.
    - Mise à jour de plusieurs dépendances pour corriger des failles de sécurité (fast-xml-builder, devalue, brace-expansion).
- **Architecture :**
    - Refonte de la gestion des erreurs pour une meilleure robustesse.
    - Factorisation de l'édition des storages.
    - Utilisation de PUT au lieu de POST pour certaines requêtes API.
    - Adaptation de la base de données pour supporter les nouvelles fonctionnalités.
- **CI/CD :**
    - Mise à jour de la version de Ruby et des dépendances Ruby.
    - Fixe la version de Node pour le déploiement.
    - Ajout de tests pour la vérification de la signature.
- **Autres :**
    - Suppression de code inutilisé et de styles obsolètes.
    - Optimisation des surcharges de dépendances.
    - Amélioration de la gestion du cache Grist.
    - Renommage de fichiers pour une meilleure organisation.

### Autres changements
- Documentation mise à jour.
- Ajout de logs pour faciliter le débogage.
- Suppression de bruit dans Sentry.
- Modification du wording d'une carte sur la page d'accueil.
- Ajout de la signature de base64.
- Mise à jour de la version de l'UI Kit.
- Suppression de jobs d'approbation.
- Utilisation de valeurs paramétrées pour MQC.
- Amélioration de la robustesse des flux.
- Filtrage des erreurs non pertinentes.
- Remplacement des cases à cocher indéterminées par des composants DSFR.
