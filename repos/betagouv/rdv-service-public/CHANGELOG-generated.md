## Changelog : rdv-service-public (30 derniers jours, au 16 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur la modernisation de l'interface utilisateur avec l'intégration du Design System Fr (DSFR), des corrections de bugs importants, notamment liés aux nouveaux noms de domaine et à l'import d'événements CalDAV, ainsi que des améliorations de la gestion des organisations et des rendez-vous. Des optimisations ont également été apportées pour faciliter l'administration et la maintenance du service.

### Évolutions fonctionnelles
- Passage du menu latéral à la version DSFR pour une meilleure cohérence visuelle et accessibilité. [#6512](https://github.com/betagouv/rdv-service-public/issues/6512)
- Amélioration de la recherche d'usagers dans l'interface d'administration (super admin) avec une recherche full-text. [#6515](https://github.com/betagouv/rdv-service-public/issues/6515)
- Affichage des liens entre les détails du motif et la réservation en ligne pour une meilleure clarté. [#6466](https://github.com/betagouv/rdv-service-public/issues/6466)
- Simplification du parcours de rendez-vous téléphonique pour une expérience utilisateur plus fluide. [#6464](https://github.com/betagouv/rdv-service-public/issues/6464)
- Ajout de l'email du bénéficiaire au parcours de prescription. [#6436](https://github.com/betagouv/rdv-service-public/issues/6436)
- Correction de l'affichage des messages flash après la connexion. [#6487](https://github.com/betagouv/rdv-service-public/issues/6487)
- Correction d'un bug empêchant le retrait de catégories d'un motif. [#6478](https://github.com/betagouv/rdv-service-public/issues/6478)
- Correction d'un bug sur l'affichage du message d'indisponibilité d'un créneau. [#6470](https://github.com/betagouv/rdv-service-public/issues/6470)
- Correction de la modification d'email usager. [#6507](https://github.com/betagouv/rdv-service-public/issues/6507)

### Évolutions techniques
- Mise à jour de Ruby vers la version 3.4.10. [#6505](https://github.com/betagouv/rdv-service-public/issues/6505)
- Refactorisation pour limiter la dépendance à Bootstrap, en utilisant davantage les utilitaires DSFR. [#6457](https://github.com/betagouv/rdv-service-public/issues/6457) et [#6460](https://github.com/betagouv/rdv-service-public/issues/6460)
- Utilisation des modales DSFR côté agent. (Annulé puis réintroduit) [#6463](https://github.com/betagouv/rdv-service-public/issues/6463) et [#6493](https://github.com/betagouv/rdv-service-public/issues/6493)
- Remplacement des alertes Bootstrap par des alertes DSFR. [#6489](https://github.com/betagouv/rdv-service-public/issues/6489)
- Remplacement des badges Bootstrap par des badges DSFR. [#6467](https://github.com/betagouv/rdv-service-public/issues/6467)
- Remplacement des boutons Bootstrap par des boutons DSFR. [#6468](https://github.com/betagouv/rdv-service-public/issues/6468)
- Utilisation de cards DSFR dans la recherche de créneaux côté agents. [#6437](https://github.com/betagouv/rdv-service-public/issues/6437)
- Ajout d'une API de gestion des webhooks pour visioplainte. [#6517](https://github.com/betagouv/rdv-service-public/issues/6517)
- Correction d'une vulnérabilité (CVE-2026-53727) dans la gem `css_parser`. [#6520](https://github.com/betagouv/rdv-service-public/issues/6520)

### Autres changements
- Migration d'organisations ouvertes à la main vers le nouveau nom de domaine. [#6518](https://github.com/betagouv/rdv-service-public/issues/6518)
- Script pour extraire toutes les organisations du territoire historique des mairies. [#6509](https://github.com/betagouv/rdv-service-public/issues/6509)
- Ajout d'une variable d'environnement pour afficher les login codes sur les environnements de revue. [#6454](https://github.com/betagouv/rdv-service-public/issues/6454)
- Marquer les agents des organisations rdv-insertion comme sensibles. [#6387](https://github.com/betagouv/rdv-service-public/issues/6387)
- Ajout d'un fichier `mise.toml` et mise à jour des instructions d'installation. [#6440](https://github.com/betagouv/rdv-service-public/issues/6440)
- Inclusion de l'identité de l'inscripteur dans l'export des participations. [#6514](https://github.com/betagouv/rdv-service-public/issues/6459)
- Possibilité de désactiver l'exécution de la tâche cron de rafraîchissement des comptes sensibles via une variable d'environnement. [#6513](https://github.com/betagouv/rdv-service-public/issues/6513)
- Correction pour les rendez-vous ANTS ajoutés avec le mauvais nom de domaine. [#6502](https://github.com/betagouv/rdv-service-public/issues/6502)
- Correction de la verticale sur le nouveau nom de domaine. [#6500](https://github.com/betagouv/rdv-service-public/issues/6500)
- Ajustements de logos et de direction de la publication pour le site vitrine. [#6483](https://github.com/betagouv/rdv-service-public/issues/6483)
- Suppression de la dépendance à `tsvector` pour la recherche par téléphone et ID. [#6349](https://github.com/betagouv/rdv-service-public/issues/6349)
- Améliorations du script pour merger des agents. [#6475](https://github.com/betagouv/rdv-service-public/issues/6475)
- Correction d'un bug JS dans l'interface d'ajout d'usagers à un RDV. [#6477](https://github.com/betagouv/rdv-service-public/issues/6477)
- Ajout d'un mock numéro ANTS RDVSPUB020 qui a des appointments. [#6476](https://github.com/betagouv/rdv-service-public/issues/6476)
- Correction d'un bug pour les créations de comptes sur le nouveau nom de domaine. [#6484](https://github.com/betagouv/rdv-service-public/issues/6484)
- Correction d'un lien raccourci pour la file d'attente. [#6471](https://github.com/betagouv/rdv-service-public/issues/6471)
- Redirection vers la liste des créneaux collectifs après inscription d'un usager. [#6469](https://github.com/betagouv/rdv-service-public/issues/6469)
- Redirection vers le bon nom de domaine. [#6479](https://github.com/betagouv/rdv-service-public/issues/6479)
- Correction de l'import d'événement CalDAV sans DTEND. [#6488](https://github.com/betagouv/rdv-service-public/issues/6488)
- Ne spécifier l'attribut CalDAV "METHOD" que dans un contexte e-mail. [#6516](https://github.com/betagouv/rdv-service-public/issues/6516)
