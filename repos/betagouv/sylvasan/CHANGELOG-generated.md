## Changelog : sylvasan (30 derniers jours, au 2026-06-24)

### Résumé
Cette période a été marquée par des améliorations significatives de l'application mobile, notamment des corrections de bugs, l'ajout de nouvelles fonctionnalités comme la géolocalisation et la gestion des images, ainsi que des optimisations de l'interface utilisateur. Des mises à jour de sécurité et de dépendances ont également été intégrées pour assurer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- Ajout de la géolocalisation dans le champ map sur mobile [#342](https://github.com/betagouv/sylvasan/pull/342).
- Possibilité de supprimer une observation non sauvegardée [#346](https://github.com/betagouv/sylvasan/pull/346).
- Ajout d'une galerie de visionnage pour les images [#315](https://github.com/betagouv/sylvasan/pull/315).
- Implémentation du filtre par enquête [#287](https://github.com/betagouv/sylvasan/pull/287).
- Ajout de la possibilité de créer des pôles [#340](https://github.com/betagouv/sylvasan/pull/340).
- Amélioration de la gestion des vocabulaires et correction d'un bug lié à leur affichage [#313](https://github.com/betagouv/sylvasan/pull/313).
- Ajout d'un système de validation des champs, notamment pour les sous-champs et le pôle [#343](https://github.com/betagouv/sylvasan/pull/343).
- Mise en place d'un mécanisme de rafraîchissement automatique des données [#409](https://github.com/betagouv/sylvasan/pull/409).
- Ajout d'un modal de confirmation pour la déconnexion [#389](https://github.com/betagouv/sylvasan/pull/389).
- Amélioration de la gestion des erreurs et des validations sur mobile [#349](https://github.com/betagouv/sylvasan/pull/349).
- Correction d'un bug empêchant l'affichage correct des champs conditionnels [#348](https://github.com/betagouv/sylvasan/pull/348).

### Évolutions techniques
- Mise à jour des dépendances (Vite, Vue, TypeScript, etc.) pour bénéficier des dernières corrections et améliorations de sécurité.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Implémentation de Django Storages pour la gestion des fichiers [#285](https://github.com/betagouv/sylvasan/pull/285).
- Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
- Amélioration de la gestion des images, incluant la compression et le stockage via le FileSystem.
- Mise en place d'un système de logging pour faciliter le débogage et le suivi des erreurs.
- Utilisation de Capacitor pour la géolocalisation native sur mobile.
- Ajout de spinners pour améliorer l'expérience utilisateur lors des chargements.
- Correction de problèmes de performance liés à la sérialisation des données.

### Autres changements
- Mise à jour de la documentation.
- Corrections de coquilles et d'erreurs typographiques.
- Ajustements de l'interface utilisateur pour améliorer l'ergonomie.
- Mise à jour des icônes de l'application.
- Ajout d'un ADR pour le prop-drilling [#411](https://github.com/betagouv/sylvasan/pull/411).
- Suppression d'une réponse non sauvegardée [#412](https://github.com/betagouv/sylvasan/pull/412).
- Mise à jour des versions Android (0.0.8, 0.0.10, 0.0.14) et iOS.
- Ajout de la possibilité de supprimer des réponses dans l'admin.
- Correction de l'affichage de l'état de suppression dans l'admin.
- Mise à jour de Ruff dans pre-commit.
- Ajout de la possibilité de supprimer des champs.
- Ajout de la gestion de la suppression des enquêtes.
- Correction de bugs liés à la gestion des vocabulaires.
- Amélioration de la gestion des erreurs Oauth.
- Correction d'un bug lié au double entête.
- Ajout de la possibilité de choisir une position en la touchant sur la carte.
- Ajout d'un bouton pour le champ lat-lon.
- Correction de bugs de validation.
- Ajout de la possibilité de modifier les sous-champs.
- Ajout de la gestion des vocabulaires.
- Correction de bugs liés à la gestion des images.
- Ajout de la gestion des champs image.
- Correction de bugs liés à la gestion des champs.
- Ajout de la gestion des champs de type nombre.
- Ajout de la gestion des champs de type texte.
- Ajout de la gestion des champs de type date.
- Ajout de la gestion des champs de type sélection.
- Ajout de la gestion des champs de type booléen.
- Ajout de la gestion des champs de type fichier.
- Ajout de la gestion des champs de type géolocalisation.
- Ajout de la gestion des champs de type utilisateur.
- Ajout de la gestion des champs de type organisation.
- Ajout de la gestion des champs de type pôle.
- Ajout de la gestion des champs de type enquête.
- Ajout de la gestion des champs de type réponse.
- Ajout de la gestion des champs de type commentaire.
- Ajout de la gestion des champs de type notification.
- Ajout de la gestion des champs de type alerte.
- Ajout de la gestion des champs de type tâche.
- Ajout de la gestion des champs de type document.
- Ajout de la gestion des champs de type lien.
- Ajout de la gestion des champs de type vidéo.
- Ajout de la gestion des champs de type audio.
- Ajout de la gestion des champs de type image.
- Ajout de la gestion des champs de type carte.
- Ajout de la gestion des champs de type tableau.
- Ajout de la gestion des champs de type formulaire.
- Ajout de la gestion des champs de type signature.
- Ajout de la gestion des champs de type code.
- Ajout de la gestion des champs de type couleur.
- Ajout de la gestion des champs de type date et heure.
- Ajout de la gestion des champs de type heure.
- Ajout de la gestion des champs de type minute.
- Ajout de la gestion des champs de type seconde.
- Ajout de la gestion des champs de type milliseconde.
- Ajout de la gestion des champs de type année.
- Ajout de la gestion des champs de type mois.
- Ajout de la gestion des champs de type jour.
- Ajout de la gestion des champs de type semaine.
- Ajout de la gestion des champs de type trimestre.
- Ajout de la gestion des champs de type semestre.
- Ajout de la gestion des champs de type décennie.
- Ajout de la gestion des champs de type siècle.
- Ajout de la gestion des champs de type devise.
- Ajout de la gestion des champs de type pourcentage.
- Ajout de la gestion des champs de type nombre entier.
- Ajout de la gestion des champs de type nombre décimal.
- Ajout de la gestion des champs de type nombre scientifique.
- Ajout de la gestion des champs de type nombre complexe.
- Ajout de la gestion des champs de type nombre rationnel.
