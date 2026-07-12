## Changelog : mon-entreprise (30 derniers jours, au 10 juillet 2026)

### Résumé
Cette mise à jour apporte des améliorations significatives à l'expérience utilisateur, notamment dans le comparateur de statuts et les simulateurs. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de l'application. L'accent a été mis sur l'accessibilité et l'amélioration de la documentation.

### Évolutions fonctionnelles
- Ajout de la carte du statut AE au choix du statut juridique.
- Amélioration de l'avertissement du simulateur concernant les dividendes.
- Ajout d'un bouton "valeurs par défaut" dans le comparateur pour réinitialiser les champs.
- Amélioration de la navigation dans le comparateur, avec un bouton pour revenir à la liste et un scroll automatique vers la question sélectionnée.
- Refonte de la mise en page du comparateur pour une meilleure lisibilité.
- Ajout d'un avertissement pour les auto-entrepreneuses dans le simulateur.
- Ajout de liens vers la documentation des objectifs de simulation.
- Correction de l'affichage des réponses dans le comparateur en vue liste.
- Correction de l'affichage des cotisations RC et ID pour les conjoints collaborateurs PLR Cipav.
- Correction de l'apparence des boutons radio.
- Ajout de l'exonération 24 mois à Mayotte dans le modèle TI.
- Correction de l'imposition de l'EI dans le comparateur.
- Ajout d'une icône d'information pour les objectifs de simulation.

### Évolutions techniques
- Refactor de l'environnement pour utiliser un adaptateur portable Vite/Next et centraliser la configuration de production.
- Suppression du client Fabrique Social inutilisé, remplacé par RechercheEntreprisesGouvFr.
- Amélioration de la gestion des erreurs Redis avec envoi d'alertes à Sentry.
- Refactor du code pour améliorer la modularité et la réutilisabilité des composants.
- Ajout de tests unitaires pour les exonérations à Mayotte.
- Mise à jour des modèles sociaux, TI et AS.
- Amélioration du tracking avec l'ajout de `trackPage` et `trackClick`.
- Uniformisation des composants de question.
- Suppression de code et de props inutilisées.
- Amélioration de l'accessibilité (a11y) de plusieurs composants (simulateur, comparateur).

### Autres changements
- Mise à jour de la documentation sur le mode d'imposition de l'entreprise.
- Correction de quelques erreurs de traduction.
- Ajout de descriptions aux règles PASS métropole.
- Mise à jour du lien vers le site QPV.
- Ajout de variables pour les tailles de police et les hauteurs de ligne dans le design system.
- Ajout de la mise à jour automatique du fichier base-stats.json tous les 6 mois.
