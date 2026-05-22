## Changelog : anssi-portail (30 derniers jours, au 21 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur la modernisation de l'interface utilisateur avec l'intégration des composants du Design System de la République Française (DSFR) sur de nombreuses pages du portail. Des corrections de bugs et des améliorations de sécurité ont également été apportées, notamment concernant la validation des entrées et la gestion des dépendances. Enfin, des améliorations ont été apportées à la gestion des guides et des filtres.

### Évolutions fonctionnelles
- Intégration des composants DSFR sur de nombreuses pages : accueil, catalogue, parcours, services, connexions, tests de maturité, etc. Cela améliore l'accessibilité et l'homogénéité visuelle du portail.
- Amélioration de la gestion des guides : affichage des assets, indication de l'absence de guide, accès aux secrets pour la lecture.
- Correction de bugs concernant le passage des filtres sur différentes pages (catalogue, financements, services, sommaire).
- Correction de la sélection des exigences et de la validation de la comparaison ReCyF.
- Ajout de la possibilité de filtrer sur les nouvelles collections.
- Correction de l'affichage des résultats des tests de maturité par défaut.
- Permet de déployer avec corepack et node 24.
- Ajout d'un encart pour le diagnostic.
- Ajout d'une animation sur l'encart des guides.
- Ajout d'un contrôle segmenté pour les parcours.

### Évolutions techniques
- Mise à jour de plusieurs dépendances pour corriger des failles de sécurité : `dompurify`, `fast-xml-parser`, `uuid`, `postcss`, `follow-redirects`, `devalue`, `brace-expansion`.
- Refactorisation du code pour utiliser les composants DSFR et supprimer du code obsolète.
- Amélioration de la robustesse des flux et gestion des erreurs réseau.
- Factorisation de l'édition des storages.
- Suppression de code inutile et simplification des surcharges de dépendances.
- Utilisation de Zod pour la validation des entrées et suppression de `express-validator`.
- Amélioration du typage des objets validés.
- Ajout de tests unitaires pour la validation des tokens.
- Suppression des jobs d’approbation.
- Utilisation des valeurs paramétrées pour MQC.
- Amélioration de la traçabilité des clics sur les liens.

### Autres changements
- Remplacement des cases à cocher indéterminées par des composants DSFR.
- Renommage du contrôle segmenté dynamique.
- Mise à jour de la page des statistiques.
- Modification du wording d'une carte sur la page d'accueil.
- Changement de "Omnicité" par "Crème de la crème".
- Suppression de styles CSS obsolètes.
- Suppression d'une page de test.
- Correction du menu "parcours débuter".
- Ajout de liens d'évitement pour l'accessibilité.
- Ajustement des styles pour réduire le CLS (Cumulative Layout Shift).
- Décodage des entrées des ressources back pour la sécurité.
- Suppression de la fonction d'aseptisation du middleware.
- Mise à jour de la version de l'UI Kit.
- Suppression des styles du header.
- Ajout de règles ESLint pour la validation des routes.
- Amélioration de la gestion des erreurs et des logs.
