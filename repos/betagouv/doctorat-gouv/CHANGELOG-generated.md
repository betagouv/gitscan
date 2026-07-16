## Changelog : doctorat-gouv (30 derniers jours, au 10 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives en matière d'accessibilité (RGAA) et de fonctionnalités de recherche, notamment avec l'intégration de la recherche vectorielle via Scaleway. Des optimisations d'interface et de l'expérience utilisateur ont également été réalisées, ainsi que des corrections de bugs et des améliorations de la documentation.

### Évolutions fonctionnelles
- Ajout d'une recherche par localisation via Scaleway et pgvector.
- Intégration de la détection d'intentions (localisation et financement) dans la recherche vectorielle, avec affichage de badges et de chips correspondants.
- Amélioration de l'affichage des résultats de recherche avec un compactage des cartes.
- Ajout de filtres Scaleway (6 filtres du formulaire) à la recherche vectorielle.
- Ajout d'un badge indiquant "En cours d'expérimentation" pour la recherche vectorielle Scaleway.
- Ajout d'un sitemap XML dynamique et d'un fichier robots.txt pour l'optimisation SEO.
- Ajout de meta descriptions sur les pages de contact, de recherche et de détail d'une thèse pour améliorer le SEO.
- Amélioration de la gestion du focus et de l'accessibilité des filtres (RGAA).
- Ajout d'aria-label aux boutons de suppression de filtres (RGAA).
- Ajout de titres de page dynamiques selon le contexte (RGAA).
- Ajout de régions live ARIA pour les mises à jour dynamiques (RGAA).
- Correction de l'accessibilité de la page détail (alertes dynamiques, liens target=_blank) (RGAA).
- Amélioration de l'accessibilité du formulaire de contact (RGAA).

### Évolutions techniques
- Intégration de Scaleway pour la recherche vectorielle.
- Mise à jour des versions pour la release 0.3.8 et 0.3.7.
- Suppression du scheduler d'indexation Albert via une propriété de configuration.
- Amélioration de la robustesse du split de la requête pour la recherche vectorielle.
- Refactor de la détection des intentions de localisation et de financement.
- Optimisation du code et de la structure pour l'accessibilité (RGAA).
- Augmentation du budget CSS pour la page de recherche.
- Ajout de logs pour les requêtes vectorielles Scaleway.

### Autres changements
- Ajout de documentation pour la release v0.3.7 (MODOP).
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Mise à jour de l'exemple NLP pour la recherche vectorielle.
- Correction de liens et de titres pour l'accessibilité (RGAA).
- Suppression du suivi git d'un fichier de livraison.
- Amélioration de la reformulation des messages d'aide et d'ambiguïté de la recherche vectorielle.
- Correction de l'attribut `lang` du document lors du changement de langue.
- Restauration des compteurs sur les sections "Meilleurs résultats" et "Autres résultats".
- Correction de l'affichage des badges de type de bloc matche Scaleway.
- Correction du lien "Aller au contenu principal".
- Ajout d'un titre sur les pages détail et contact.
- Correction de la hiérarchie de titres (RGAA).
- Ajout d'un lien d'évitement vers le contenu principal (RGAA).
- Ajout de labels accessibles aux champs de recherche des dropdowns (RGAA).
- Remplacement des flèches du carrousel par des boutons DSFR tertiaires.
- Remplacement des points du carrousel par des flèches de navigation.
