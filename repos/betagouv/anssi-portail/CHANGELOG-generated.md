## Changelog : anssi-portail (30 derniers jours)

### Résumé
Ce changelog résume les évolutions récentes du portail ANSSI. Les modifications portent principalement sur l'amélioration de l'expérience utilisateur, notamment avec la refonte de la page d'accueil, l'ajout de nouvelles fonctionnalités comme la page directive NIS2 et la demande de diagnostic cyber, ainsi que des corrections de bugs et des optimisations de performance. Des améliorations techniques ont également été apportées, notamment concernant la gestion des statistiques et la sécurité des dépendances.

### Évolutions fonctionnelles
- Refonte de la page d'accueil avec une nouvelle présentation et des illustrations.
- Ajout d'une page dédiée à la directive NIS2, incluant des onglets, une vidéo et la possibilité de télécharger la plaquette.
- Implémentation d'une nouvelle fonctionnalité de demande de diagnostic cyber, avec une version WebComponent pour une intégration facilitée.
- Amélioration du suivi des téléchargements avec l'ajout de l'origine du téléchargement.
- Ajout de statistiques dynamiques sur la page d'accueil.
- Possibilité de contacter le DPD (Délégué à la Protection des Données) via une nouvelle section dédiée.
- Ajout de liens vers des nouvelles pages dans le pied de page.
- Amélioration de la gestion des guides : masquage des guides non publiés et tri par date de publication/mise à jour.
- Ajout d'un bouton de redirection vers les guides depuis l'accueil.
- Amélioration de la page statistiques.

### Évolutions techniques
- Mise à jour de plusieurs dépendances pour améliorer la sécurité et la performance (UI-Kit, diff).
- Optimisation du cache pour les résultats de MAC (Mesures d'Atténuation du Cyber-risque).
- Refonte de l'intégration des statistiques depuis l'API.
- Amélioration de la gestion des événements avec la publication d'un événement `VisaTelecharge`.
- Utilisation de Grist pour la gestion des guides et des ressources.
- Implémentation d'un workflow de comparaison des guides entre deux sources.
- Suppression des feature flags pour les guides, les filtres de comparaison et les avis.
- Correction de plusieurs vulnérabilités potentielles et améliorations de la sécurité.
- Amélioration de la structure du code et refactoring de certains composants.

### Autres changements
- Mise à jour de la documentation et des instructions d'installation.
- Correction de typos et amélioration de la formulation de certains textes.
- Amélioration de la conformité aux standards d'accessibilité.
- Ajustements de style et de mise en page pour une meilleure expérience utilisateur.
- Ajout de commentaires et de documentation pour faciliter la maintenance du code.
- Mise en place d'un système de logs plus complet pour faciliter le débogage.
- Suppression de code inutilisé et nettoyage du code source.
